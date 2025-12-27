from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import Dataset
import json


@login_required
def dataset_list(request):
    datasets = Dataset.objects.filter(owner=request.user).order_by("-updated_at")
    return render(
        request,
        "pyramydal_core/dataset_list.html",
        {"datasets": datasets},
    )


@login_required
def dataset_detail(request, dataset_id):
    dataset = get_object_or_404(Dataset, id=dataset_id, owner=request.user)
    rows = dataset.rows.all()

     # HTMX request: return only the table
    if request.headers.get("HX-Request"):
        html = render_to_string(
            "pyramydal_core/_dataset_rows.html",
            {"rows": rows},
            request=request,
        )
        return HttpResponse(html)

    # normal full-page renderer
    return render(
        request,
        "pyramydal_core/dataset_detail.html",
        {
            "dataset": dataset,
            "rows": rows,
        },
    )

@require_POST
@login_required
def update_row(request, row_id):
    row = get_object_or_404(
        DatasetRow,
        id=row_id,
        dataset__owner=request.user,
    )

    try:
        data = json.loads(request.POST["data"])
    except json.JSONDecodeError:
        return HttpResponse("Invalid JSON", status=400)

    row.data = data
    row.save()

    rows = row.dataset.rows.all()

    return render(
        request,
        "pyramydal_core/_dataset_rows.html",
        {"rows": rows},
    )
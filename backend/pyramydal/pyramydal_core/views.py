from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from .models import Dataset


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
    return render(
        request,
        "pyramydal_core/dataset_detail.html",
        {
            "dataset": dataset,
            "rows": rows,
        },
    )

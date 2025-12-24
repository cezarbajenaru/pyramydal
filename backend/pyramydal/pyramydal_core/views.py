from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required
def spread_home(request):
    return HttpResponse("Spreadsheet platform home")


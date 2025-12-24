from django.urls import path
from .views import dataset_list, dataset_detail

urlpatterns = [
    path("", dataset_list, name="dataset_list"),
    path("<int:dataset_id>/", dataset_detail, name="dataset_detail"),
]

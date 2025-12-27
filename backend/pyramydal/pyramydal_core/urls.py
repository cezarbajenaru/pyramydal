from django.urls import path
from .views import dataset_list, dataset_detail, update_row

urlpatterns = [
    path("", dataset_list, name="dataset_list"),
    path("<int:dataset_id>/", dataset_detail, name="dataset_detail"),
    path("row/<int:row_id>/update/", update_row, name="update_row"),
]

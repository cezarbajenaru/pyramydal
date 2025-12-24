from django.contrib import admin
from .models import Dataset, DatasetRow


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "created_at", "updated_at")
    list_filter = ("owner",)
    search_fields = ("name",)
    ordering = ("-updated_at",)


@admin.register(DatasetRow)
class DatasetRowAdmin(admin.ModelAdmin):
    list_display = ("id", "dataset", "row_index", "created_at")
    list_filter = ("dataset",)
    ordering = ("dataset", "row_index")

from django.contrib import admin
from .models import Dataset, DatasetVersion, DatasetRow


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "current_version", "created_at")
    list_filter = ("owner",)
    search_fields = ("name",)
    ordering = ("-updated_at",)


@admin.register(DatasetVersion)
class DatasetVersionAdmin(admin.ModelAdmin):
    list_display = ("id", "dataset", "version_number", "created_at")
    list_filter = ("dataset",)
    ordering = ("-version_number",)


@admin.register(DatasetRow)
class DatasetRowAdmin(admin.ModelAdmin):
    list_display = ("id", "version", "row_index", "created_at")
    list_filter = ("version",)
    ordering = ("version", "row_index")

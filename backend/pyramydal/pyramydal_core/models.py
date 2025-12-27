from django.conf import settings
from django.db import models


class Dataset(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="datasets",
    )
    current_version = models.ForeignKey(
        "DatasetVersion",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DatasetVersion(models.Model):
    dataset = models.ForeignKey(
        Dataset,
        on_delete=models.CASCADE,
        related_name="versions",
    )
    version_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("dataset", "version_number")
        ordering = ["-version_number"]

    def __str__(self):
        return f"{self.dataset.name} v{self.version_number}"


class DatasetRow(models.Model):
    version = models.ForeignKey(
        DatasetVersion,
        on_delete=models.CASCADE,
        related_name="rows",
    )
    row_index = models.PositiveIntegerField()
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["row_index"]
        indexes = [
            models.Index(fields=["version", "row_index"]),
        ]

    def __str__(self):
        return f"{self.version} row {self.row_index}"
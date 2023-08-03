from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    """Room or Experience Category"""

    class Meta:
        verbose_name_plural = "Categories"

    class CategoryKindChoice(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(
        max_length=11,
        choices=CategoryKindChoice.choices,
    )

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"

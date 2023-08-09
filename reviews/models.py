from django.db import models
from common.models import CommonModel
from django.conf import settings


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    payload = models.TextField()
    rating = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"

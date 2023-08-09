from django.db import models
from common.models import CommonModel
from django.conf import settings


class ChattingRoom(CommonModel):

    """ChattingRoom Model Definition"""

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="chatting_rooms",
    )

    def __str__(self) -> str:
        return f"Chatting Room."


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"

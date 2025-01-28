from django.db import models
from common.models import CommonModel


class MessageRoom(CommonModel):
    """MessageRoom Model Definition"""

    participants = models.ManyToManyField(
        "users.User",
    )

    def __str__(self):
        return "Message Room"


class Message(CommonModel):
    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    message_room = models.ForeignKey(
        "direct_messages.MessageRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}: {self.text}"

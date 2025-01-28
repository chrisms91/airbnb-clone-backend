from django.contrib import admin
from .models import MessageRoom, Message


@admin.register(MessageRoom)
class MessageRoomAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )

    list_filter = ("created_at",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = (
        "text",
        "user",
        "message_room",
        "created_at",
    )

    list_filter = ("created_at",)

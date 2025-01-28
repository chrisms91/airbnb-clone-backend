from django.db import models
from common.models import CommonModel

# Create your models here.


class Experience(CommonModel):
    """Experience Model Definition"""

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50, default="South Korea")
    city = models.CharField(max_length=100, default="Seoul")
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start_at = models.TimeField()
    end_at = models.TimeField()
    description = models.TextField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    category = models.ForeignKey(
        "categories.Category", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    details = models.CharField(max_length=250, blank=True, default="")
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name

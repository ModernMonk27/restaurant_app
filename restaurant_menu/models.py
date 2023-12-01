from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("tiffen", "Tiffen"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("starters", "Starters"),
    ("deserts", "Deserts")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=1000)
    meal_type = models.CharField(max_length=1000, choices=MEAL_TYPE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

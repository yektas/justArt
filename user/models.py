from django.contrib.auth.models import User
from django.db import models

from main.models import Category


class Result(models.Model):
    user = models.ForeignKey(User, related_name="result")
    category = models.ForeignKey(Category, related_name="player")
    point = models.IntegerField()
    played_date = models.DateTimeField(auto_now_add=True)
    support_point = models.IntegerField()
    play_count = models.IntegerField()

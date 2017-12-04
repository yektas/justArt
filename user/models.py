from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from main.models import Category
from support.models import Foundation
from support.signals import support_added


class Result(models.Model):
    user = models.ForeignKey(User, related_name="result")
    category = models.ForeignKey(Category, related_name="player")
    point = models.IntegerField()
    played_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Result of user " + self.user.username


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", related_name="profile", on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0)
    support_count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        UserProfile.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=Result)
def update_user_play_count(sender, **kwargs):
    if kwargs['created']:
        user = UserProfile.objects.get(user=kwargs['instance'].user)
        user.play_count += 1
        user.save()


@receiver(support_added, sender=Foundation)
def update_user_support_count(sender, **kwargs):
    user = User.objects.get(pk=kwargs['user_id'])
    user.profile.support_count += 1
    user.profile.save()


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

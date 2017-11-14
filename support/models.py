from django.db import models
from django.shortcuts import get_object_or_404

from support.signals import support_added


class FoundationManager(models.Manager):
    def add_support(self, user, foundation_id):
        foundation = get_object_or_404(Foundation, pk=foundation_id)
        foundation.support_count += 1
        foundation.save()
        support_added.send(
            sender=Foundation,
            user_id=user.id
        )
        return foundation.support_count

    def get_support_count(self):
        foundations = Foundation.objects.all()
        count = 0
        for foundation in foundations:
            count += foundation.support_count
        return count


class Foundation(models.Model):
    foundation_name = models.CharField(max_length=255)
    logo = models.ImageField()
    about = models.TextField()
    support_count = models.IntegerField(default=0, editable=False)

    objects = FoundationManager()

    def __str__(self):
        return self.foundation_name

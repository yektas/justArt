from django.db import models
from django.shortcuts import get_object_or_404


class FoundationManager(models.Manager):
    def add_support(foundation_id):
        foundation = get_object_or_404(Foundation, pk=foundation_id)
        foundation.support_count += 1
        foundation.save()
        return foundation.support_count

    def get_support_count():
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

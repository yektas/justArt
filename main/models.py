from random import randint

from django.db import models
from django.db.models import Count
from django.utils.safestring import mark_safe


class RandomManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class Question(models.Model):
    questionImage = models.ImageField()
    answer = models.ForeignKey("Artist", related_name="question")
    point = models.IntegerField(null=True, blank=True)
    category = models.ManyToManyField("Category", related_name="category")

    def __str__(self):
        return self.questionImage.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.questionImage.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class Artist(models.Model):
    artist_name = models.CharField(unique=True, max_length=200)
    movement_name = models.ForeignKey("Art_Movement", related_name="artist")
    objects = models.Manager()
    randoms = RandomManager()

    def __str__(self):
        return self.artist_name


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Art_Movement(models.Model):
    movement_name = models.CharField(max_length=200)

    def __str__(self):
        return self.movement_name

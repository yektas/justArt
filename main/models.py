from django.db import models


class Question(models.Model):
    questionImage = models.ImageField()
    answer1 = models.ForeignKey("Answer", related_name="answer1")
    answer2 = models.ForeignKey("Answer", related_name="answer2")
    answer3 = models.ForeignKey("Answer", related_name="answer3")
    answer4 = models.ForeignKey("Answer", related_name="answer4")
    point = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey("Category", related_name="level")


class Answer(models.Model):
    answer = models.CharField(max_length=200)


class Category(models.Model):
    category_name = models.CharField(max_length=200)

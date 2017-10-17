from django.db import models


class Question(models.Model):
    questionImage = models.ImageField()
    answer1 = models.ForeignKey("Answer", related_name="answer1")
    answer2 = models.ForeignKey("Answer", related_name="answer2")
    answer3 = models.ForeignKey("Answer", related_name="answer3")
    answer4 = models.ForeignKey("Answer", related_name="answer4")
    point = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey("Category", related_name="level")

    def __str__(self):
        return self.questionImage.name

    @property
    def get_content(self):
        image_url = str(self.questionImage)
        answers = (str(self.answer1), str(self.answer2), str(self.answer3), str(self.answer4))
        category = str(self.category)
        point = str(self.point)
        content = (image_url, answers, category, point)
        return content


class Answer(models.Model):
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.answer


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

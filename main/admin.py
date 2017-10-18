from django.contrib import admin

from main.models import Question, Choice, Category

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Category)

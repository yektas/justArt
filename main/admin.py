from django.contrib import admin

from main.models import Question, Choice, Category


class QuestionStyle(admin.ModelAdmin):
    readonly_fields = ('image_tag',)


admin.site.register(Question, QuestionStyle)
admin.site.register(Choice)
admin.site.register(Category)

from django.contrib import admin

from main.models import Question, Category, Art_Movement, Artist


class QuestionStyle(admin.ModelAdmin):
    readonly_fields = ('image_tag',)
    filter_horizontal = ('category',)

admin.site.register(Question, QuestionStyle)
admin.site.register(Artist)
admin.site.register(Art_Movement)
admin.site.register(Category)

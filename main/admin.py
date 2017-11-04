from django.contrib import admin

from main.models import Question, Category, Art_Movement, Artist


class QuestionStyle(admin.ModelAdmin):
    fields = ('image_tag', 'questionImage', 'answer', 'point', 'category')
    readonly_fields = ('image_tag',)
    filter_horizontal = ('category',)
    list_display = ('image_tag', 'answer', 'point')


class ArtistStyle(admin.ModelAdmin):
    list_display = ('artist_name', 'movement_name')

admin.site.register(Question, QuestionStyle)
admin.site.register(Artist, ArtistStyle)
admin.site.register(Art_Movement)
admin.site.register(Category)

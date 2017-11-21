from django.contrib import admin

from user.models import Result, UserProfile


class ResultStyle(admin.ModelAdmin):
    fields = ('user', 'category', 'point', 'played_date')
    readonly_fields = ('user', 'category', 'point', 'played_date')
    list_display = ('user', 'category', 'point', 'played_date')


class UserProfileStyle(admin.ModelAdmin):
    fields = ('user', 'play_count', 'support_count')
    readonly_fields = ('play_count', 'support_count')
    list_display = ('user', 'play_count', 'support_count')


admin.site.register(Result, ResultStyle)
admin.site.register(UserProfile, UserProfileStyle)

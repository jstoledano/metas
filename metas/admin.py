# coding: utf-8

from django.contrib import admin
from .models import Goal


class GoalAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'role', 'key')
    list_filter = ('role',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


admin.site.register(Goal, GoalAdmin)

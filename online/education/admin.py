from django.contrib import admin

# Register your models here.

from .models import Test


class Testinfoadmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'introduction', 'date']


admin.site.register(Test, Testinfoadmin)


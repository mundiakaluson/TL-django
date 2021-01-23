from django.contrib import admin
from . import models

class OrderAdmin(admin.ModelAdmin):

    list_display = ('topic', 'style', 'words', 'level', 'deadline', 'price')
    list_filter = ('topic', 'deadline', 'price')

admin.site.register(models.Order, OrderAdmin)


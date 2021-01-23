from django.contrib import admin
from . import models

admin.site.register(models.Order)

class OrdersAdmin(admin.ModelAdmin):

    fields = ('topic', 'deadline')

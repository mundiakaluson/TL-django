from django.contrib import admin
from . import models

class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'topic', 'style', 'words', 'level', 'deadline', 'price')
    list_filter = ('topic', 'deadline', 'price')
    readonly_fields = ('id', )

class BidAdmin(admin.ModelAdmin):

    list_display = ('id', 'user_bid', 'bid_selected')

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Bid, BidAdmin)
admin.site.site_header = 'Tutoring Learners Terminal'

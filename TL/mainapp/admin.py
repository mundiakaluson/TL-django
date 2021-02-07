from django.contrib import admin
from . import models
from django.contrib.auth.models import User
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'topic', 'style', 'words', 'level', 'deadline', 'price')
    list_filter = ('topic', 'deadline', 'price')
    readonly_fields = ('id', )
    list_per_pages = 20

<<<<<<< HEAD
class BidAdmin(admin.ModelAdmin):

    list_display = ('order_id', 'order_topic', 'bid_note', 'bidder')
    readonly_fields = ['order_id', 'order_topic', 'bid_note', 'bidder']


=======
>>>>>>> 1ba393cb26e33683f0aeaca01e79c4ed4c2ee48c
admin.site.register(models.Order, OrderAdmin)
admin.site.site_header = 'Tutoring Learners Terminal'
admin.site.index_title = 'TL Admin Panel'


from django.contrib import admin
from django.http import request
from django.shortcuts import render
from . import models
class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'topic', 'style', 'words', 'level', 'deadline', 'price')
    list_filter = ('topic', 'deadline', 'price')
    readonly_fields = ('id', )
    list_per_pages = 20

class BidAdmin(admin.ModelAdmin):

    list_display = ('order_id', 'order_topic', 'bid_note', 'bidder')
    readonly_fields = ['order_id', 'order_topic', 'bid_note', 'bidder']
        
class AssignAdmin(admin.ModelAdmin):
    
    change_form_template = 'admin/change_form.html'
    list_display = ('writer_assigned', 'order_assigned')
    actions = ['assign_order_action']

    def assign_order_action(self, request):

        if request.POST['writer_assigned'] and request.POST['order_assigned']:
            order = models.Order()
            order_object = models.Assign()
            order_object.writer_assigned = request.POST['writer_assigned']
            order_object.order_assigned = request.POST['order_assigned']
            order_object.save()

            return render(request, 'admin/change_form.html', {'order_object': order_object , 'order': order})


admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Bid, BidAdmin)
admin.site.register(models.Assign, AssignAdmin)
admin.site.site_header = 'Tutoring Learners Terminal'
admin.site.index_title = 'TL Admin Panel'


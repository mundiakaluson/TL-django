from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('user','phone', 'profession', 'ranking', 'rating')
    list_filter = ('profession', 'ranking', 'rating')
    readonly_fields = ('user', )


admin.site.register(Profile, ProfileAdmin)
admin.site.index_title = 'User Profiles and Management'
admin.site.site_header = 'TL Employee Management'

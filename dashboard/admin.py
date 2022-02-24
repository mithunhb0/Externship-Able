from django.contrib import admin
from dashboard.models import Lead



class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone_number', 'created_at','updated_at')
    list_display_links = ('id','name','email')
    readonly_fields = ('updated_at', 'created_at')
    ordering = ('-id',)

admin.site.register(Lead, LeadAdmin)


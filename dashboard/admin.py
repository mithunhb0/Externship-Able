from django.contrib import admin
from dashboard.models import Lead, Remark



class LeadAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'phone_number', 'created_at','updated_at')
    list_display_links = ('id','name','email')
    readonly_fields = ('updated_at', 'created_at')
    ordering = ('-id',)

admin.site.register(Lead, LeadAdmin)

class RemarkAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','remark_area', 'created_at','updated_at')
    list_display_links = ('id','user_id')
    readonly_fields = ('updated_at', 'created_at')
    ordering = ('-id',)

admin.site.register(Remark, RemarkAdmin)
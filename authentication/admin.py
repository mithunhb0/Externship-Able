from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import Account



class AccountAdmin(UserAdmin):
    list_display = ('id','email', 'first_name', 'last_name', 'last_login', 'created_at')
    list_display_links = ('id','email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'created_at')
    ordering = ('-created_at',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
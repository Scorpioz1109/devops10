from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

class UserProfileAdmin(UserAdmin):
    list_display = (
        'username',
        'password',
        'phone',
        'staff_id',
        'job_status',
    )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('员工个人信息'), {'fields': ('phone', 'staff_id','job_status')}),
    )


admin.site.register(UserProfile , UserProfileAdmin)
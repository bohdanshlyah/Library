from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import UserAdminCreationForm
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = UserAdminCreationForm
    list_display = ('id', 'email',)
    readonly_fields = ('updated_at', 'created_at',)
    ordering = ('id',)
    empty_value_display = '-empty-'

    fieldsets = (
        (None, 
        {'fields': ('email', 'password', 'first_name', 'middle_name', 
                   'last_name', 'role',
                   'is_active', 'is_staff', 'is_superuser')
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'first_name', 'middle_name', 
                       'last_name',   'role',
                       'is_active', 'is_staff', 'is_superuser')
        }),
    )

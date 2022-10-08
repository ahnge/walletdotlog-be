from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    model = CustomUser

    list_display = ('email', 'id', 'full_name', 'is_active', 'is_staff')
    list_filter = ('email', 'full_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'image', 'social_image')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'image', 'social_image', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

    search_fields = ('email', 'full_name')
    ordering = ('-created_at',)


admin.site.register(CustomUser, CustomUserAdmin)

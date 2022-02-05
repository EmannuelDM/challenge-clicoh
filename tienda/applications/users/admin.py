from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('pk', 'email', 'full_name',)
    list_display_links = ('pk', 'email', 'full_name',)

    search_fields = (
        'email',
    )

    list_filter = (
        'is_active',
        'is_staff',
       
    )


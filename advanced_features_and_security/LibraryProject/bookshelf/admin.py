from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy

# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ['publication_year']
    search_fields = ['title', 'author']

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['Username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (gettext_lazy('Additional info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (gettext_lazy('Additional Info'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
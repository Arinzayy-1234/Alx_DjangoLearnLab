from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import CustomUser


# Register your models here.

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('date_of_birth', 'profile_photo',)

    fieldsets = UserAdmin.fieldsets + ((None,{'fields': ('date_of_birth','profile_photo',)}), )

    add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields': ('date_of_birth','profile_photo',)}),)
admin.site.register(Book,BookAdmin,)
admin.site.register(CustomUser, CustomUserAdmin)

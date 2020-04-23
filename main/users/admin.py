from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from main.users.models import MyUser, Profile


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )


@admin.register(Profile)
class MyProfile(admin.ModelAdmin):
    list_display = ('user', 'bio', 'address')

from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Dweet



admin.site.unregister(User)


class ProfileInLine(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username','email', 'password']
    inlines = [ProfileInLine]


admin.site.unregister(Group)
admin.site.register(Dweet)

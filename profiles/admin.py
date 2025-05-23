# profiles/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from django.contrib.auth.models import User

admin.site.register(Profile)

# Optionally unregister/re-register User if needed
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

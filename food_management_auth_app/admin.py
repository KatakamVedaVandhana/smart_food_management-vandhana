# your django admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from food_management_auth_app.models.user import User

admin.site.register(User, UserAdmin)

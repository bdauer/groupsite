from django.contrib import admin

# Register your models here.
from .models import Invitation, UserGroup, UserProfile

admin.site.register(Invitation)
admin.site.register(UserGroup)
admin.site.register(UserProfile)

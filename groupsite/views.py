from django.shortcuts import render
from django.http import (HttpResponse, HttpRequest)
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

# Profile
#   name, avatar, bio.
#
# Edit Profile
#   name, avatar, bio.

# Groups
# My groups
#   name, description. Click to edit.
# Pending invites
# name, description, inviter, accept, decline.

# Create Group
#   name
#   description

# Manage Group (only my groups)
#   name, dscription, invite, current users

from django.shortcuts import render
from django.http import (HttpResponse, HttpRequest, HttpResponseRedirect)
from django.core.urlresolvers import reverse_lazy
# Create your views here.
def index(request):
    return render(request, 'groupsite/index.html')


def login(request):
    return render(request, 'groupsite/login.html')


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

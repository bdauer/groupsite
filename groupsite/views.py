from django.shortcuts import render
from django.views import generic
from django.http import (HttpResponse, HttpRequest, HttpResponseRedirect)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserGroup, Invitation

# Create your views here.
def index(request):
    return render(request, 'groupsite/index.html')


def login(request):
    return render(request, 'groupsite/login.html')


class GroupsView(LoginRequiredMixin, generic.ListView):
    """
    Show all of a user's groups and invitations.
    """
    template_name = "groupsite/groups.html"
    model = UserGroup

    def get_context_data(self, **kwargs):
        data = super(generic.ListView, self).get_context_data(**kwargs)
        request = self.request
        data['groups'] = UserGroup.objects.get_user_groups(request.user)
        data['sent_invites'] = Invitation.objects.get_pending_sent_invites(
                                                                    request.user)
        data['received_invites'] = Invitation.objects.get_pending_received_invites(
                                                                        request.user)
        return data

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

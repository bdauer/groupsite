from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import (HttpResponse, HttpRequest, HttpResponseRedirect)
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
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

class CreateGroupView(LoginRequiredMixin, generic.CreateView):
    """
    Create a new group.
    """
    template_name = "groupsite/creategroup.html"
    model = UserGroup
    fields = ['name', 'description', 'members']

    # def get_absolute_url(self):
    #     return reverse("update group", kwargs={'pk': self.pk})

    def get_success_url(self):
        return reverse_lazy('groupsite:groups')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.save()
        form.instance.members.add(self.request.user)
        form.save()
        return super(CreateGroupView, self).form_valid(form)

class ManageGroupView(LoginRequiredMixin, generic.UpdateView):
    """
    Update a group.
    """
    # def get_object(self):
    #     object = UserGroup.objects.get(pk=self.kwargs['id'])
    template_name = "groupsite/creategroup.html"
    model = UserGroup
    fields = ['description', 'members']

    def get_success_url(self):
        return reverse_lazy('groupsite:groups')

class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View detailed information about a group.
    """
    template_name = "groupsite/groupdetail.html"
    model = UserGroup



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


# Manage Group (only my groups)
#   name, dscription, invite, current users

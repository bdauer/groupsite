from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import (HttpResponse, HttpRequest, HttpResponseRedirect,
                         JsonResponse)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms
from .models import UserGroup, Invitation, UserProfile
from .forms import CreateInviteForm

# Create your views here.
def index(request):
    return render(request, 'groupsite/index.html')


def login(request):
    return render(request, 'groupsite/login.html')


def update_invite(request):
    """
    Accept or decline an invite.
    """
    if request.is_ajax():
        invite_id = request.POST['invite_id']
        status = request.POST['new_status']
        print(status)
        invite = Invitation.objects.get(pk=invite_id)

        if status == "accepted":
            invite.status = "A"
            group = invite.user_group
            group.members.add(request.user)
            group.save()
        elif status == "declined":
            invite.status = "D"
        invite.save()
    return HttpResponse()

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

class CreateInviteView(LoginRequiredMixin, generic.CreateView):
    """
    Create a new invite.
    """
    template_name = "groupsite/createinvite.html"
    form_class = CreateInviteForm

    def get_success_url(self):
        return reverse_lazy('groupsite:groups')

    def get_form_kwargs(self):
        kwargs = super(CreateInviteView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    # need to override user_group to only show groups for the current user.

    def form_valid(self, form):
        form.instance.invitor = self.request.user
        form.save()
        return super(CreateInviteView, self).form_valid(form)

class CreateGroupView(LoginRequiredMixin, generic.CreateView):
    """
    Create a new group.
    """
    template_name = "groupsite/creategroup.html"
    model = UserGroup
    fields = ['name', 'description']

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
    template_name = "groupsite/creategroup.html"
    model = UserGroup
    fields = ['description']

    def get_success_url(self):
        return reverse_lazy('groupsite:groups')

class GroupDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View detailed information about a group.
    """
    template_name = "groupsite/groupdetail.html"
    model = UserGroup

class ManageProfile(LoginRequiredMixin, generic.UpdateView):
    """
    Edit your profile
    """
    template_name = "groupsite/manageprofile.html"
    model = UserProfile
    fields = ['avatar','bio']

    def get_success_url(self):
        print(self.request.user)
        return reverse_lazy('groupsite:profile details', kwargs={"pk":self.request.user.pk})

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View your profile.
    """
    template_name = "groupsite/profiledetail.html"
    model = UserProfile

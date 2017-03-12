from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class UserGroupManager(models.Manager):

    def get_user_groups(self, user):
        """
        Return all groups that have the user as a member.
        """
        pass

class UserGroup(models.Model):
    """
    Group for users. Not to be confused with the auth groups.

    name: the name of the group.
    description: a brief description of the group.
    creator: the creator of the group, endowed with administrative capabilities.
    members: members of the group.
    """
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(default=None, null=True)
    creator = models.ForeignKey(User, related_name='usergroup_creator')
    members = models.ManyToManyField(User, related_name='usergroup_members')


class UserProfile(models.Model):
    """
    Extension of the base User class for storing profile info.

    user: the associated user.
    avatar: the visual representation of the user.
    bio: a little bit about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=None, null=True)
    bio = models.TextField(default=None, null=True)



class InvitationManager(models.Manager):

    def get_pending_sent_invites(self, user):
        """
        Return all pending sent invites.
        """
        pass

    def get_pending_received_invites(self, user):
        """
        Return all pending received invites.
        """
        pass


class Invitation(models.Model):
    """
    Invitations are extended by a group creator to allow membership in their group.
    """
    user_group = models.OneToOneField(UserGroup)
    invitor = models.ForeignKey(User, related_name='invitor')
    invitee = models.ForeignKey(User, related_name='invitee')

    STATUSES = ( ('A', 'accepted'),
                 ('D', 'declined'),
                 ('P', 'pending'),
            )
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              default='P')

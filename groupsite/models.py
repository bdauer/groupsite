from __future__ import unicode_literals

from django.db import models

# Create your models here.

class GroupManager(models.Manager):

    def get_user_groups(self, user):
        """
        Return all groups that have the user as a member.
        """
        pass

class Group(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    creator = models.OneToOneField(User)
    users = models.ManyToManyField(User)


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

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
    group = models.OneToOneField(Group)
    invitor = models.OneToOneField(User)
    invitee = models.OneToOneField(User)

    STATUSES = ( ('A', 'accepted'),
                 ('D', 'declined'),
                 ('P', 'pending'),
            )
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              default='P')

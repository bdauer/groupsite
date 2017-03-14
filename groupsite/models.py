from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.

class UserGroupManager(models.Manager):

    def get_user_groups(self, user):
        """
        Return all groups that have the user as a member.
        """
        return self.filter(members=user)

    def get_created_groups(self, user):
        """
        Return all groups created by the user.
        """
        return self.filter(creator=user)

class UserGroup(models.Model):
    """
    Group for users. Not to be confused with the auth groups.

    name: the name of the group.
    description: a brief description of the group.
    creator: the creator of the group, endowed with administrative capabilities.
    members: members of the group.
    """
    objects = UserGroupManager()
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(default=None, null=True)
    creator = models.ForeignKey(User, related_name='usergroup_creator')
    members = models.ManyToManyField(User, related_name='usergroup_members')

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    Extension of the base User class for storing profile info.

    user: the associated user.
    avatar: the visual representation of the user.
    bio: a little bit about the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default=None, null=True, upload_to='photos/')
    bio = models.TextField(default=None, null=True)



class InvitationManager(models.Manager):

    def get_pending_sent_invites(self, user):
        """
        Return all pending sent invites.
        """
        return self.filter(invitor=user,
                           status='P')

    def get_pending_received_invites(self, user):
        """
        Return all pending received invites.
        """
        return self.filter(invitee=user,
                           status='P')


class Invitation(models.Model):
    """
    Invitations are extended by a group creator to allow membership in their group.
    """
    objects = InvitationManager()
    user_group = models.ForeignKey(UserGroup)
    invitor = models.ForeignKey(User, related_name='invitor')
    invitee = models.ForeignKey(User, related_name='invitee')

    STATUSES = ( ('A', 'accepted'),
                 ('D', 'declined'),
                 ('P', 'pending'),
            )
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              default='P')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    When a new user is created, creates a profile for them.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    When a new user is created, saves their profile.
    """
    instance.userprofile.save()

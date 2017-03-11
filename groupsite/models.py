from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    creator = models.OneToOneField(User)


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

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

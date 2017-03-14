from django import forms
from django.contrib.auth.models import User
from .models import Invitation, UserGroup


class CreateInviteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CreateInviteForm, self).__init__(*args, **kwargs)
        self.fields['user_group'].queryset =\
                                UserGroup.objects.get_created_groups(
                                                                user=self.user)
        self.fields['invitee'].queryset =\
                            User.objects.all().exclude(pk=self.user.pk)
    class Meta:
        model = Invitation
        fields = ['user_group', 'invitee']

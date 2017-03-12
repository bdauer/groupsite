from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def save_user(backend, user, response, *args, **kwargs):
    """
    Save a user created through a socialauth pipeline.
    """
    try:
        profile = user.userprofile
    except ObjectDoesNotExist:
        profile = UserProfile(user_id=user.id)
    if backend.name == 'facebook':
        profile.facebook_id = response.get('id')
    if backend.name == 'google-oauth2':
        try:
            profile.google_id = response.get('id')
            profile.save()
        except OverflowError:
            profile.google_id = response.get('id')[0:15]

    return {'profile': profile}

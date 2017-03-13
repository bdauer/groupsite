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
    return {'profile': profile}

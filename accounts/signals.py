from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token

from accounts.models import Profile, LibraryUser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created=False, **kwargs):
    try:
        Profile.objects.get_or_create(user=instance)
        Token.objects.get_or_create(user=instance)
    except Exception as e:
        print(e)
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class LibraryUser(AbstractUser):
    pass

    def __str__(self):
        return "{} {}".format(self.last_name, self.first_name)


class Profile(models.Model):
    '''
    Create a profile attached to the user from which we will attach a task story and an auth token
    '''
    STORY_ONE = 'story one'
    STORY_TWO = 'story two'
    STORY_THREE = 'story three'
    STORY_CHOICES = (
        ('story one', STORY_ONE),
        ('story two', STORY_TWO),
        ('story three', STORY_THREE)
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='user_profile')
    story = models.CharField(max_length=15, choices=STORY_CHOICES, null=True, blank=True, default=STORY_ONE)

    def __str__(self):
        return self.user.username

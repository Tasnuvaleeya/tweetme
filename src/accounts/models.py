from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    # user.profile find the profile for the user
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    # profile.user.following user i follow
    # user.followed_by user that follow me

    def __str__(self):
        return str(self.following.all().count())
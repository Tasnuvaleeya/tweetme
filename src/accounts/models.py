from django.db import models
from django.conf import settings

# Create your models here.


class UserProfileManager(models.Manager):
    def all(self):
        qs = self.get_queryset().all()
        print(self)
        print(self.instance)
        try:
            if self.instance:
                qs = qs.exclude(user = self.instance)
        except:
            pass
        return qs


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    # user.profile find the profile for the user
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
    # profile.user.following user i follow
    # user.followed_by user that follow me
    objects = UserProfileManager()

    def __str__(self):
        return str(self.following.all().count())

    def get_following(self):
        users = self.following.all()
        return users.exclude(username=self.user.username)
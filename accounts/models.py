from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save

# Create your models here.

# All stuff here is to connect new users to the models we've created

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    city = models.CharField (max_length= 100, default="")
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

#def create_profile(sender, **kwargs):
#    if kwargs['created']:
#        user_profile=UserProfile.objects.create(user=kwargs['instance'])


# post_save.connect(create_profile, sender = User)"""


# Create your models here.
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    email = models.EmailField(max_length=150)
    date_modified = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile_signal(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
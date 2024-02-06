from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField



class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = ImageField(default='user-temp.png', upload_to="profiles/")
    bio = models.TextField(max_length=500)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Creates a profile on creation of User, to be customsed"""
    if created:
        Profile.objects.create(user=instance)
    
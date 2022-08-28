from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    nameCN = models.CharField(max_length=100,null=True)
    twitch_id = models.CharField(max_length=100)

    @receiver(post_save, sender=get_user_model())
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=get_user_model())
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

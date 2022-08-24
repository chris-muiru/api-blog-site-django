from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import LikeModel


@receiver(post_save, sender=LikeModel)
def DeleteFalseLikeInstance(sender, instance, **kwargs):
    if instance.is_liked == False:
        instance.delete()

from django.dispatch import receiver
from django.db.models.signals import post_save
from allauth.socialaccount.models import SocialAccount


@receiver(post_save, sender=SocialAccount)
def add_name_and_img(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.full_name = instance.extra_data.get('name')
        if instance.provider == "github":
            user.image_url = instance.extra_data.get('avatar_url')
        if instance.provider == "google":
            user.image_url = instance.extra_data.get('picture')
        user.save()

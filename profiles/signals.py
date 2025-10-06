from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
import logging

logger = logging.getLogger('profiles.signals')


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    try:
        if created:
            UserProfile.objects.create(user=instance)
            logger.info(f"Created profile for user: {instance.username}")
        else:
            # Only save existing profile if it exists
            try:
                instance.userprofile.save()
            except UserProfile.DoesNotExist:
                UserProfile.objects.create(user=instance)
                logger.info(f"Created missing profile for existing user: {instance.username}")
    except Exception as e:
        logger.error(f"Error creating/updating profile for user {instance.username}: {str(e)}")
        # Don't raise the exception to prevent registration failure
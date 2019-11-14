from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Dprofile

@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
	user = instance
	if created:
		dprofile = Dprofile(user=user)
		dprofile.save()
		#testing
	# 	Dprofile.objects.create(user=instance)
	# instance.dprofile.save()

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
# 	instance.dprofile.save()

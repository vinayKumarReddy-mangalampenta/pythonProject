from django.conf import settings
from django.db.models.signals import post_save, post_delete

from django.contrib.auth.models import User
from django.dispatch import receiver

from users.models import Profile
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        data = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        subject = 'welcome'
        welcomeMsg = 'Hi {} , welcome to dev search we are glad to be here.'.format(
            user.username)
        send_mail(
            subject,
            welcomeMsg,
            settings.EMAIL_HOST_USER,
            [data.email],
            fail_silently=False,
        )


@receiver(post_delete, sender=Profile)
def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()


# post_save.connect(createProfile,sender=User)
# post_delete.connect(deleteUser,sender=Profile)

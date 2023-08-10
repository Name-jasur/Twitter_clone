from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _



class Profile(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username}"
            f"{self.image}"
            f"({self.data:%Y-%m-%d-%H:%M}):"
        )


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance,)
        user_profile.save()
        # user_profile.follows.add(instance.profile)
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


post_save.connect(create_profile, sender=User)


class Dweet(models.Model):
    user = models.ForeignKey(User,
                             related_name='dweets',
                             on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user}"
            f"({self.created_at:%Y-%m-%d-%H:%M}):"
            f"{self.body[:30]}..."
        )


class StaffLogin(models.Model):
    staff = models.ForeignKey(
        Profile,
        verbose_name=_("Staff"),
        on_delete=models.CASCADE,
        related_name='user_stafflogin',
        limit_choices_to={'is_staff': True},
    )

    session_key = models.CharField(
        max_length=40,
        verbose_name=_("Session Key"),
    )




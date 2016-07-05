from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.signals import post_save


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )
    # DefaultUser
    # Django Model은 Meta => abstart=True (테이블 생성 X)라고 되어있지 않으면,
    # 모델을 상속할 수 없도록 되어있음

# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     # User:UserProfile = 1:1
#     # user => UserProfile ( O ) ==> post_save signal
# post_save.connect( , sender=User)
# @receiver(post_save, sender=User)
# def post_save_user(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=intance)

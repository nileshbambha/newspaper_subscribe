from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# class userprofile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     phone_number = models.IntegerField()
#     gender = models.CharField(max_length=20)
#     user_type =  models.CharField(max_length=20)
#     address =  models.CharField(max_length=20)
#     city =  models.CharField(max_length=20)
#     state =  models.CharField(max_length=20)
#     pincode = models.IntegerField()
     
#     def __str__(self):
#         return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         userprofile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()
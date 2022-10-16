from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=2000,null=True,blank=True)
    username=models.CharField(max_length=200,null=True,blank=True)
    headline = models.TextField(null=True,blank=True)
    profile_img = models.ImageField(null=True,blank=True,upload_to='static/userprofile')
    social_github = models.CharField(max_length=200,null=True,blank=True)
    social_twitter = models.CharField(max_length=200,null=True,blank=True)
    social_linkedin = models.CharField(max_length=200,null=True,blank=True)
    social_youtube = models.CharField(max_length=200,null=True,blank=True)
    social_website = models.CharField(max_length=200,null=True,blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid4,primary_key=True)
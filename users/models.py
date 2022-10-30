from uuid import uuid4
from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=2000, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    headline = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_img = models.ImageField(
        null=True, blank=True, upload_to='static/userprofile', default="static/userprofile/user-default.png")
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True,unique=True,editable=False)

    def __str__(self) -> str:
        return self.username


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True,unique=True,editable=False)

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL,related_name="sender")
    receiver = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL,related_name="receiver")
    subject = models.CharField(max_length=1500)
    body = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, primary_key=True,unique=True,editable=False)

    def __str__(self) -> str: 
        return self.subject

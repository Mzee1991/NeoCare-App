from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RegistrationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=30)
    token = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(default=timezone.now)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nin_no = models.CharField(max_length=100, default='CMX10000000')
    contact = models.CharField(max_length=100, default='+256 ')
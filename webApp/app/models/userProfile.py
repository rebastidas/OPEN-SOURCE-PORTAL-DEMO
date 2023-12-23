from django.db import models
from users.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    bio = models.TextField(max_length=3000)
    phone = models.CharField(max_length=16)
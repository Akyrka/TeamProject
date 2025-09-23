from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, verbose_name="Про себе")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Профіль {self.user.username}"

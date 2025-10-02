from django.db import models
from django.contrib.auth.models import User
from electronic_diary.models import SchoolClass  # импортируем класс

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, verbose_name="Про себе")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, null=True, blank=True, related_name="students")

    def __str__(self):
        return f"{self.user.username} ({self.school_class})"

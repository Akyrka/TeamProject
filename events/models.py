from django.db import models
from django.conf import settings
# Create your models here.
class Event(models.Model):
    STATUS_CHOICES = [
        ('Пройшов', "Пройшов"),
        ('Проходить',"Проходить"),
        ("Буде проходити", "Буде проходити")


    ]
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Буде проходити")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="events"


    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


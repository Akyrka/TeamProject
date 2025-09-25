from django.db import models
from django.conf import settings
class ForumThread(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="threads"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ForumPost(models.Model):
    thread =  models.ForeignKey(
        ForumThread,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    text = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Виставлено {self.author} в {self.thread}"





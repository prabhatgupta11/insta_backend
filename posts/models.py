
# Create your models here.
# posts/models.py
from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=50)
    caption = models.TextField()

    def __str__(self):
        return f"{self.username}: {self.caption}"

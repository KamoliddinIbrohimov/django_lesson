from django.db import models

# Create your models here.
class Todo(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
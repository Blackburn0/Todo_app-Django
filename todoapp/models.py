from django.db import models


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=100)
    task = models.TextField()

    def __str__(self):
        return self.name
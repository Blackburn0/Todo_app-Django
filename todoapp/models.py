from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')   
    name = models.CharField(max_length=100)
    task = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
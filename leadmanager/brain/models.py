from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects",on_delete=models.CASCADE, null=True)
    is_created = models.BooleanField(default=False)
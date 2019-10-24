from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects",on_delete=models.CASCADE, null=True)
    is_created = models.BooleanField(default=False)
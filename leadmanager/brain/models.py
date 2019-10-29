from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    project_name = models.CharField(default='', max_length=250)
    user = models.ForeignKey(User, related_name="projects",on_delete=models.CASCADE, null=True)
    brain_project_id = models.IntegerField(default=0)
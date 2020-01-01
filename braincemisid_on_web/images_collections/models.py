from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImagesFromNeuron(models.Model):
    owner = models.ForeignKey(User, related_name="images_collection", on_delete=models.CASCADE, null=True)
    name=models.CharField(default='', max_length=250)
    name_class=models.CharField(default='', max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    img64 = models.FileField(upload_to='uploads/')
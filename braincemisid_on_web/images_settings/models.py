from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from brain.models import brain
from images_collections.models import ImagesFromNeuron 
from django.contrib.auth.models import User


# Create your models here.

class ImageSettings (models.Model):
    r_tolerance = models.FloatField(default=0,validators=[MaxValueValidator(1), MinValueValidator(0)])
    g_tolerance = models.FloatField(default=0,validators=[MaxValueValidator(1), MinValueValidator(0)])
    b_tolerance = models.FloatField(default=0,validators=[MaxValueValidator(1), MinValueValidator(0)])
    brain = models.ForeignKey(brain, related_name="brain",on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(ImagesFromNeuron, related_name="image",on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, related_name="imageSettings", on_delete=models.CASCADE, null=True)
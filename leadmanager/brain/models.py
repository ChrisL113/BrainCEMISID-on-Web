from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class projects(models.Model):
    snb_s= models.BinaryField(null=True)
    snb_h= models.BinaryField(null=True)
    rnb= models.BinaryField(null=True)
    am_net= models.BinaryField(null=True)
    gnb= models.BinaryField(null=True)
    syllables_net= models.BinaryField(null=True)
    words_net= models.BinaryField(null=True)
    ss_rnb= models.BinaryField(null=True)
    episodic_memory= models.BinaryField(null=True)
    decisions_block= models.BinaryField(null=True)
    internal_state= models.BinaryField(null=True)
    desired_state= models.BinaryField(null=True)
    user = models.ForeignKey(User, related_name="brain", on_delete=models.CASCADE, null=True)
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class brain_proto(models.Model):
    snb_s= models.BinaryField()
    snb_h= models.BinaryField()
    rnb= models.BinaryField()
    am_net= models.BinaryField()
    gnb= models.BinaryField()
    syllables_net= models.BinaryField()
    word_net= models.BinaryField()
    ss_rnb= models.BinaryField()
    episodic_memory= models.BinaryField()
    decisions_block= models.BinaryField()
    internal_state= models.BinaryField()
    desired_state= models.BinaryField()
    user_id = models.ForeignKey(User, related_name="brain", on_delete=models.CASCADE, null=True)
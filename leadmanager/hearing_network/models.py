from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
# Create your models here.

class brain_proto(models.Model):
    user = models.ForeignKey(User, related_name="brains",on_delete=models.CASCADE, null=True)
    
class snb_s(models.Model):
    brain=models.OneToOneField(
        brain_proto,
        related_name="snb_s",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _state = models.CharField(max_length=280, default= 'MISS?')
    _index_ready_to_learn = models.IntegerField()
    _last_learned_id = models.IntegerField()

#brain_proto.objects.filter(snb_s__rbf_neurons=None)

class RbfNeuron(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="rbf_neurons",on_delete=models.CASCADE, null=True)
    _has_knowledge = models.BooleanField()
    _radius = models.FloatField()
    _degraded = models.FloatField()
    _knowledge = JSONField()


class IndexRecognize(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="index_recognize",on_delete=models.CASCADE, null=True)
    index_recognize = models.IntegerField() 
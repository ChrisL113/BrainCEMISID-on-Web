from django.db import models
from brain.models import projects
from django.contrib.postgres.fields import JSONField

# Create your models here.

    
class snb_s(models.Model):
    brain_project=models.OneToOneField(
        projects,
        related_name="snb_s_json",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _state = models.CharField(max_length=280, default= 'MISS?')
    _index_ready_to_learn = models.IntegerField()
    _last_learned_id = models.IntegerField()

    def __str__(self):
        return self.brain_project.id
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
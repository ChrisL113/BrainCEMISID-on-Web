from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
# Create your models here.

class brain(models.Model):
    name=models.CharField(default='', max_length=250)
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



class snb_s(models.Model):
    brain_s=models.OneToOneField(
        brain,
        related_name="snb_s_json",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    state = models.CharField(max_length=280, default= 'MISS?')
    index_ready_to_learn = models.IntegerField()
    last_learned_id = models.IntegerField()


class RbfNeuronSight(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="rbf_neuron",on_delete=models.CASCADE, null=True)
    has_knowledge = models.BooleanField()
    radius = models.FloatField()
    degraded = models.BooleanField()
    knowledge = JSONField(null=True,blank=True)


class IndexRecognizeSight(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="index_recognize",on_delete=models.CASCADE, null=True)
    index_recognize = models.IntegerField() 


class snb_h(models.Model):
    brain_h=models.OneToOneField(
        brain,
        related_name="snb_h_json",
        on_delete=models.CASCADE,
        primary_key=True,
    )
    state = models.CharField(max_length=280, default= 'MISS?')
    index_ready_to_learn = models.IntegerField()
    last_learned_id = models.IntegerField()


class RbfNeuronHearing(models.Model):
    snb_hearing = models.ForeignKey(snb_h, related_name="rbf_neuron",on_delete=models.CASCADE, null=True)
    has_knowledge = models.BooleanField()
    radius = models.FloatField()
    degraded = models.BooleanField()
    knowledge = JSONField(null=True,blank=True)


class IndexRecognizeHearing(models.Model):
    snb_hearing = models.ForeignKey(snb_h, related_name="index_recognize",on_delete=models.CASCADE, null=True)
    index_recognize = models.IntegerField() 
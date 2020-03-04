from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from images_collections.models import ImagesFromNeuron
# Create your models here.

class brain(models.Model):
    name=models.CharField(default='', max_length=250)
    am_net= models.BinaryField(null=True)
    gnb= models.BinaryField(null=True)
    syllables_net= models.BinaryField(null=True)
    words_net= models.BinaryField(null=True)
    episodic_memory= models.BinaryField(null=True)
    decisions_block= models.BinaryField(null=True)
    internal_state= JSONField(null=True,blank=True)
    desired_state= JSONField(null=True,blank=True)
    user = models.ForeignKey(User, related_name="brain", on_delete=models.CASCADE, null=True)

class rnb(models.Model):
    brain_rnb=models.OneToOneField(
        brain,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    index_ready_to_learn=models.IntegerField()

class ss_rnb(models.Model):
    brain_ss_rnb=models.OneToOneField(
        brain,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    index_ready_to_learn=models.IntegerField()

class SsRnbNeuron(models.Model):
    ss_rnb = models.ForeignKey(ss_rnb, related_name="ss_rnb_neuron",on_delete=models.CASCADE, null=True)
    has_knowledge = models.BooleanField()
    hit = models.BooleanField()
    knowledge = JSONField(null=True,blank=True)

class RnbNeuron(models.Model):
    rnb = models.ForeignKey(rnb, related_name="rnb_neuron",on_delete=models.CASCADE, null=True)
    has_knowledge = models.BooleanField()
    hit = models.BooleanField()
    knowledge = JSONField(null=True,blank=True)

class snb_s(models.Model):
    brain_s=models.OneToOneField(
        brain,
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
    img= models.ForeignKey(ImagesFromNeuron, related_name="image_related", on_delete=models.SET_NULL,null=True)


class IndexRecognizeSight(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="index_recognize",on_delete=models.CASCADE, null=True)
    index_recognize = models.IntegerField() 


class snb_h(models.Model):
    brain_h=models.OneToOneField(
        brain,
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


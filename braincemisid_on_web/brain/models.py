from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from images_collections.models import ImagesFromNeuron
# Create your models here.

class brain(models.Model):
    name = models.CharField(default='', max_length=250)
    ######################################################## REVISION ###########################################################
    gnb = models.BinaryField(null=True)
    am_net_proto = models.BinaryField(null=True)
    ################################################################################################################################
    decisions_block = models.BinaryField(null=True)

    internal_state = JSONField(null=True,blank=True)
    desired_state = JSONField(null=True,blank=True)
    user = models.ForeignKey(User, related_name="brain", on_delete=models.CASCADE, null=True)


############################################################ am_net ##############################################

class am_net(models.Model):
    brain_am_net = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField(default=0)
    clack = models.BooleanField()
    indexes_recognized = JSONField(null=True,blank=True)

class group_am_net(models.Model):
    am_net_group = models.ForeignKey(am_net, related_name="am_net_group",on_delete=models.CASCADE, null=True)
    index_bip = models.IntegerField()
    AmNetNeuron = JSONField(null=True,blank=True)


############################################################ Syllables_net ##############################################

class syllables_net(models.Model):
    brain_syllables_net = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField(default=0)
    clack = models.BooleanField()
    indexes_recognized = JSONField(null=True,blank=True)

class group_syllables_net(models.Model):
    syllables_net_group = models.ForeignKey(syllables_net, related_name="syllables_net_group",on_delete=models.CASCADE, null=True)
    index_bip = models.IntegerField()
    SyllaNetNeuron = JSONField(null=True,blank=True)


############################################################ Words_net ##############################################

class words_net(models.Model):
    brain_words_net = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField(default=0)
    clack = models.BooleanField()
    indexes_recognized = JSONField(null=True,blank=True)

class group_words_net(models.Model):
    words_net_group = models.ForeignKey(words_net, related_name="words_net_group",on_delete=models.CASCADE, null=True)
    index_bip = models.IntegerField()
    WordNetNeuron = JSONField(null=True,blank=True)


############################################################ Episodic Memories ##############################################

class episodic_memory(models.Model):
    brain_episodic_memory = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField(default=0)
    clack = models.BooleanField()
    indexes_recognized = JSONField(null=True,blank=True)

class group_episode(models.Model):
    episodic_memory_group = models.ForeignKey(episodic_memory, related_name="episode_group",on_delete=models.CASCADE, null=True)
    index_bip = models.IntegerField()
    episodicMemNeuron = JSONField(null=True,blank=True)

############################################################ Rel Network ##############################################

class rnb(models.Model):
    brain_rnb=models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField()

class ss_rnb(models.Model):
    brain_ss_rnb = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    index_ready_to_learn = models.IntegerField()

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



############################################################ Sensory Neural Block ##############################################

class snb_s(models.Model):
    brain_s = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
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
    img = models.ForeignKey(ImagesFromNeuron, related_name="image_related", on_delete=models.SET_NULL,null=True)


class IndexRecognizeSight(models.Model):
    snb_sight = models.ForeignKey(snb_s, related_name="index_recognize",on_delete=models.CASCADE, null=True)
    index_recognize = models.IntegerField() 


class snb_h(models.Model):
    brain_h = models.OneToOneField(
        brain,
        on_delete = models.CASCADE,
        primary_key = True,
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



# ########### gnb
# class knowledge_GNB(models.Model):
#     neuron=models.OneToOneField(
#         Neuron,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )

# class gnb(models.Model):
#     _operation= models.CharField(default="COUNT", max_length=50)
#     _op2_queue =
# 	_zero =
# 	_op1_queue =
# 	_operator =
# 	_add_operator =
#     _equal_sign =

# class QuantityOrderGroup(models.Model):
#     _has_quantity = models.BooleanField(default=False)

# class QuantityNeuron(models.Model):
#     quantityOrderGroup=models.OneToOneField(
#         QuantityOrderGroup,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     ####################################POR DEFINIR###################################
#     _has_knowledge= models.BooleanField(default=False)

# class OrderNeuron(models.Model):
#     quantityOrderGroup=models.OneToOneField(
#         QuantityOrderGroup,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     ####################################POR DEFINIR###################################
#     _has_knowledge= models.BooleanField(default=False)

# class QuantityOrderNetwork(models.Model):
#     Gnb=models.OneToOneField(
#         gnb,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     group_list = models.ArrayModelField(
#         model_container = QuantityOrderGroup
#     )
#     _index = models.IntegerField()


# class AdditionStructure(models.Model):
#     index = models.IntegerField()
#     neurons = models.ArrayModelField(
#         model_container = Neuron
#     )
#     Gnb=models.OneToOneField(
#         gnb,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
#     carry_over = models.BooleanField(default=False)

# #################### decisions block

# class decisions_block(models.Model):
#     inputs_memories
#     unconscious_block
#     desired_state
#     conscious_output
#     internal_state
#     conscious_block
#     unconscious_output
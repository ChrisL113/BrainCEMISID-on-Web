from django.contrib.auth.models import User
from djongo import models
from django import forms
# Create your models here.



class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


class snb(models.Model):
    _last_learned_ids= models.ArrayModelField(
        model_container=models.IntegerField(),
        default=-1
    )

class snb_s(models.Model):
    Snb=models.OneToOneField(
        snb,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _state = models.CharField(max_length=280, default= 'MISS?')
    _index_ready_to_learn = models.IntegerField(default= 0)
    _last_learned_id = models.IntegerField(default= -1)

class RbfNeuron_s(models.Model):
    Snb_s = models.ForeignKey(snb_s, on_delete=models.CASCADE)
    _has_knowledge = models.BooleanField(default= False)
    _radius = models.FloatField(default=24)
    _degraded = models.BooleanField(default= False)
    _index_recognize = models.ArrayModelField(
        model_container= models.IntegerField()
    )


#################################################### SNB ######################################################
class knowledge_s(models.Model):
    RBfNeuron_s=models.OneToOneField(
        RbfNeuron_s,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _pattern = models.ArrayModelField(
        model_container= models.IntegerField(default=0)
    ) 
    _class = models.CharField(default='hearing ID', max_length=150)
    _set = models.CharField(default='NoSet', max_length=150)

class snb_h(models.Model):
    Snb=models.OneToOneField(
        snb,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class RbfNeuron_h(models.Model):
    Snb_h = models.ForeignKey(snb_h, on_delete=models.CASCADE)
    _has_knowledge = models.BooleanField(default= False)
    _radius = models.FloatField(default=24)
    _degraded = models.BooleanField(default= False)
    _index_recognize = models.ArrayModelField(
        model_container= models.IntegerField(),
        default=-1
    ) 

class knowledge_h(models.Model):
    RBfNeuron_h=models.OneToOneField(
        RbfNeuron_h,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _pattern = models.ArrayModelField(
        model_container= models.IntegerField(default=0)
    ) 
    _class = models.CharField(default='hearing ID', max_length=150)
    _set = models.CharField(default='NoSet', max_length=150)

#################################################### RNB ######################################################

class RelNeuron(models.Model):
    _hit= models.BooleanField(default=False)
    _has_knowledge = models.BooleanField(default= False)

class rnb(models.Model):
    _index_ready_to_learn = models.IntegerField()
    neuron_list = models.ArrayModelField(
        model_container = RelNeuron 
    )

class knowledge_rnb(models.Model):
    RELNeuron=models.OneToOneField(
        RelNeuron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    _h_id = models.IntegerField()
    _s_id = models.IntegerField()
    _weight = models.IntegerField()

#################################################### AM_NET ######################################################

class CulturalNeuron(models.Model):
    ####################################POR DEFINIR###################################
    pass

class CulturalGroup(models.Model):
    _index_bip = models.IntegerField()
    group = models.ArrayModelField(
        model_container = CulturalNeuron     
    )

class am_net(models.Model):
    _clack = models.BooleanField(default=False)
    _index_ready_to_learn = models.IntegerField()
    group_list = models.ArrayModelField(
        model_container= CulturalGroup
        #,model_form_class=
    )  

#################################################### GNB ######################################################

class Neuron(models.Model):
    _has_knowledge= models.BooleanField(default=False)

class knowledge_GNB(models.Model):
    neuron=models.OneToOneField(
        Neuron,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ####################################POR DEFINIR###################################

class gnb(models.Model):
    _operation= models.CharField(default="COUNT", max_length=50)
    """ _op2_queue =
	_zero =
	_op1_queue =
	_operator =
	_add_operator =
    _equal_sign = """

class QuantityOrderGroup(models.Model):
    _has_quantity = models.BooleanField(default=False)

class QuantityNeuron(models.Model):
    quantityOrderGroup=models.OneToOneField(
        QuantityOrderGroup,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ####################################POR DEFINIR###################################
    _has_knowledge= models.BooleanField(default=False)

class OrderNeuron(models.Model):
    quantityOrderGroup=models.OneToOneField(
        QuantityOrderGroup,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ####################################POR DEFINIR###################################
    _has_knowledge= models.BooleanField(default=False)

class QuantityOrderNetwork(models.Model):
    Gnb=models.OneToOneField(
        gnb,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    group_list = models.ArrayModelField(
        model_container = QuantityOrderGroup
    )
    _index = models.IntegerField()


class AdditionStructure(models.Model):
    index = models.IntegerField()
    neurons = models.ArrayModelField(
        model_container = Neuron
    )
    Gnb=models.OneToOneField(
        gnb,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    carry_over = models.BooleanField(default=False)

#################################################### Syllables ######################################################

class syllables(models.Model):
    _clack = models.BooleanField(default= False)
    _index_ready_to_learn = models.IntegerField()
    group_list =  models.ArrayModelField(
        model_container = CulturalGroup
    )
    _recognized_indexes = models.ArrayModelField(
        model_container = models.IntegerField(),
        default=-1
    )

#################################################### words_net ######################################################

class words_net(models.Model):
    _clack = models.BooleanField(default= False)
    _index_ready_to_learn = models.IntegerField()
    group_list =  models.ArrayModelField(
        model_container = CulturalGroup
    )
    _recognized_indexes = models.ArrayModelField(
        model_container = models.IntegerField(),
        default=-1
    )

#################################################### ss_rnb ######################################################

class ss_rnb(models.Model):
    neuron_list = models.ArrayModelField(
        model_container = RelNeuron
    )
    _index_ready_to_learn = models.IntegerField()


#################################################### episodic memory ######################################################

class episodic_memory(models.Model):
    _clack = models.BooleanField(default=False)
    _index_ready_to_learn = models.IntegerField()
    group_list = models.ArrayModelField(
        model_container=CulturalGroup
    )
    _recognized_indexes = models.ArrayModelField(
        model_container= models.IntegerField(),
        default=-1
    ) 

####################################################  decisions block ######################################################

class internalState(models.Model):
    culture = models.FloatField(default=0.5)
    biology = models.FloatField(default=0.5)
    feelings = models.FloatField(default=0.5)

class decisions_block(models.Model):
    pass
    #inputs_memories
#    unconscious_block
 #   desired_state
    #conscious_output
  #  internal_state
   # conscious_block
    #unconscious_output

#################################################### state ######################################################
class internal_state(internalState):
    pass

class desired_state(internalState):
    pass

""" class CulturalGroup_form(forms.ModelForm):
        class Meta:
            model = CulturalGroup_form
            fields = ('','') """
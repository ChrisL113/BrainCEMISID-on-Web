from rest_framework import serializers
from images_settings.models import ImageSettings

class ImagesSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model= ImageSettings
        fields = '__all__'

class ImageSettingsWithImageFromNeuron(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    name_class = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()


    class Meta:
        model= ImageSettings
        fields = ['id','r_tolerance','g_tolerance','b_tolerance','image','img','created','name','name_class','created','owner']
    
    def get_img(self,obj):
        return obj.image.img.url
    def get_created(self,obj):
        return obj.image.created.__str__()
    def get_name(self, obj):
        return obj.image.name
    def get_name_class(self,obj):
        return obj.image.name_class
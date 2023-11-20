from rest_framework import serializers
from . import models

class FormOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Form1
        fields = "__all__"



class FormTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FormTwo
        fields = "__all__"
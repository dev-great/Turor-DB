from rest_framework import serializers
from .models import *

class Tutorserializer(serializers.ModelSerializer):
    class Meta:
        model = TutorModel
        fields= '__all__'


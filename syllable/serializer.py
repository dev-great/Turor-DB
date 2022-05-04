from rest_framework import serializers
from .models import *

class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields= '__all__'

class Syllableserializer(serializers.ModelSerializer):
    class Meta:
        model = Syllable
        fields= '__all__'
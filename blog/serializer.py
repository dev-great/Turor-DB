from rest_framework import serializers
from .models import *

class Feedserializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields= '__all__'

class FeedVideoserializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPostVideo
        fields= '__all__'
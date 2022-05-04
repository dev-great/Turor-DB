from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.utils.decorators import method_decorator


User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',
                  'first_name', 'last_name', 'email',)
        extra_kwargs = {'password': {"write_only": True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class Profileserializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class Paymentserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'


class Subscriptionserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'


class Gettutorserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Gettutor
        fields = '__all__'


class Locationserializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class Classserializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class Activetutorserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Activetutor
        fields = '__all__'


class Becometutorserializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Becometutor
        fields = '__all__'


class Workserializer(serializers.ModelSerializer):
    tutor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Workhistory
        fields = '__all__'


class Educationserializer(serializers.ModelSerializer):
    tutor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Educationalhistory
        fields = '__all__'

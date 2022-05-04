from django.shortcuts import render
from .models import *
from .serializer import *
from datetime import datetime
from rest_framework import generics
from rest_framework import status
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_auth.views import PasswordResetView
# Create your views here.


class CustomPasswordResetView(PasswordResetView):
    pass


class PaymentView(APIView, ):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get_serializer_class(self):
        return Paymentserializer

    def get(self, request):
        username = request.user.username
        user = User.objects.get(username__exact=username)
        detail = user.username

        paymentHistory = Payment.objects.filter(user=user)
        serializer = Paymentserializer(paymentHistory, many=True)
        return Response(serializer.data)

    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        username = request.user.username
        user = User.objects.get(username__exact=username)

        serializers = Paymentserializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=user)
            return Response(serializers.data)
        return Response(Paymentserializer)


class SubscriptionView(APIView, ):

    def get_serializer_class(self):
        return Subscriptionserializer

    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        username = request.user.username
        user = User.objects.get(username__exact=username)

        serializers = Subscriptionserializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=user)
            return Response(serializers.data)
        return Response(Subscriptionserializer)


class ProfileView(APIView, ):

    def get_serializer_class(self):
        return Profileserializer

    def get(self, request):
        username = request.user.username
        user = User.objects.get(username__exact=username)
        detail = user.username

        profile = Profile.objects.filter(user=user)
        serializer = Profileserializer(profile, many=True)
        return Response(serializer.data)

    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        username = request.user.username
        user = User.objects.get(username__exact=username)

        serializers = Profileserializer(data=request.data)
        if serializers.is_valid():
            serializers.save(user=user)
            return Response(serializers.data)
        return Response(Profileserializer)


class RegisterView(APIView):
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Userserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response({"error": True})


class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Workserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationalView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Educationserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class ActivetutorView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Activetutorserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class BecomeTutorView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Becometutorserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class GettutorView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    csrf_protect_method = method_decorator(csrf_protect)

    def post(self, request):
        serializers = Gettutorserializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"error": False})
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

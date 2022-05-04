from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class SubjectView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        subjects = Subjects.objects.all()
        serializer = Subjectserializer(subjects, many = True)
        return Response(serializer.data)

class SyllableView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        syllables = Syllable.objects.all()
        serializer = Syllableserializer(syllables, many = True)
        return Response(serializer.data)

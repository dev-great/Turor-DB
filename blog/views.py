from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class FeedView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        feeds = FeedPost.objects.all()
        serializer = Feedserializer(feeds, many = True)
        return Response(serializer.data)

class FeedViewVideo(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    def get(self, request):
        feedvideos = FeedPostVideo.objects.all()
        serializer = FeedVideoserializer(feedvideos, many = True)
        return Response(serializer.data)

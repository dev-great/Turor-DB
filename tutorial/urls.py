from django.urls import path  
from . import views

urlpatterns=[
    path('teacher/', views.TutorView.as_view()),
]
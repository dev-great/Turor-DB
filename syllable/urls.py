from django.urls import path  
from . import views

urlpatterns=[
    path('subject/', views.SubjectView.as_view()),
    path('syllable/', views.SyllableView.as_view()),
]
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_protect

urlpatterns = [
    path('login/', csrf_protect(obtain_auth_token)),
    path('register/', RegisterView.as_view()),
    path('logout/', Logout.as_view()),
    path('profile/', ProfileView.as_view()),
    path('payment/', PaymentView.as_view()),
    path('becometutor/', BecomeTutorView.as_view()),
    path('gettutor/', GettutorView.as_view()),
    path('activetutor/', ActivetutorView.as_view()),
    path('workexperience/', WorkView.as_view()),
    path('educational/', EducationalView.as_view()),
    path('subscription/', SubscriptionView.as_view()),
    path('changepassword/', ChangePasswordView.as_view()),
    path('password_reset/', include('django_rest_passwordreset.urls',
         namespace='password_reset')),
]
# /api/

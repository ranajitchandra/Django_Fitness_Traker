from django.urls import path
from calorieApp.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', signinPage, name='signinPage'),
    path('signupPage/', signupPage, name='signupPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('addfood/', addfood, name='addfood'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

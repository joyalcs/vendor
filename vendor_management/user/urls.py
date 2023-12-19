from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('api-token-auth/', views.CustomAuthToken.as_view(), name='custom-auth-token')
]

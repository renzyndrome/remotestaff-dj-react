from django.urls import path

from .views import UserRegister, UserLogin

urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
    path('login', UserLogin.as_view(), name='login'),
    path('logout', UserLogin.as_view(), name='logout'),
    path('user', UserLogin.as_view(), name='user'),
    
]

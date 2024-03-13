from django.urls import path
from .views import home, login, register, logoutUser

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
]
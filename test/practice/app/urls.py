from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logoutUser, name='logout'),
    
    path('create/', create_blog, name='create'),
    path('getAllBlog/', get_all_blog, name='getAllBlog'),
    path('getBlog/<int:pk>/', get_blog, name='getBlog'),
    path('updateBlog/<int:pk>/', update_blog, name='updateBlog'),
    path('delete/<int:pk>/', delete_blog, name='delete'),
]
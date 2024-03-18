from django.urls import path
from .views import *

urlpatterns = [
    path('', myView.as_view(name="Anil")),
    path('child/', MyViewChild.as_view()),
]

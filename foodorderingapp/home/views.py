from django.shortcuts import render
from .models import Pizza

# Create your views here.
def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'home.html', context)
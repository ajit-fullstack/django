from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
# def home(requset):
#     return HttpResponse('<p>Testing</p>')

class myView(View):
    name = "Ajit"
    def get(self, request):
        return HttpResponse(self.name)
    
class MyViewChild(myView):
    def get(self, requset):
        return render(requset, 'school/home.html')
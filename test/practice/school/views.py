from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ContactForm

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
    
def contactForm(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {"form": form})

class ContactFormView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank You Form Submitted !!')

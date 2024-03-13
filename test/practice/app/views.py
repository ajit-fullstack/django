from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as userLogin, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username =username)
        except:
            print('User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            userLogin(request, user)
            return redirect('home')
    return render(request, 'app/login.html')

def register(request):
    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password')
        # print(username, password, confirm_password)
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user =  form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            userLogin(request, user)
            return redirect('home')
        else:
            print('You are making some mistake')

    return render(request, 'app/signup.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

def create_blog(request):
    pass

def get_all_blog(request):
    pass

def get_blog(request, pk):
    pass

def update_blog(request, pk):
    pass

def delete_blog(request, pk):
    pass

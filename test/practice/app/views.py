from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as userLogin, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm
from .models import Blog
from django.http import HttpResponse

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
    users = User.objects.all()
    context = {'users': users}
    if request.method == 'POST':
        data = dict(request.POST)
        data.update({"user": 1, "category": 'Python'})
        form = BlogForm(data)
        print(form, data)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('error')
    return render(request, 'app/blog.html', context)

def get_all_blog(request):
    blog = Blog.objects.all()
    return render(request, 'app/bloglist.html', {'blogs': blog})
    

def get_blog(request, pk):
    pass

def update_blog(request, pk):
    item = Blog.objects.get(id=pk)
    form = BlogForm(instance=item)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('app/home')
        
    context = {"form": form}
    return render(request, 'app/blog.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('app/home')
    return HttpResponse('Blog has been deleted sucessfully')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message
from .form import RoomForm
from django.db.models import Q


# Create your views here.
def loginPage(request):
    page = "login"
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or password is invalid")
    context = {"page": page}
    return render(request, "base/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during regestration')

    context = {"page": page, "form": form}
    return render(request, 'base/login_register.html', context)

def home(request):

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q) 
    )

    room_count = rooms.count()

    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics, "room_count": room_count}

    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(pk=pk)
    room_message = room.message_set.all().order_by('-created')

    if request.method == 'POST':
        message = Message.objects.create(
            room= room,
            user= request.user,
            body= request.POST.get('body')
        )
        return redirect('room', pk=room.id)

    context = {"room": room, "room_message": room_message}
    return render(request, "base/room.html", context)


@login_required(login_url="login")
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/app/home")
        
    context = {"form": form}
    return render(request, "base/room_form.html", context)

@login_required(login_url="login")
def updateRoom(request, pk):
    item = Room.objects.get(id=pk)
    form = RoomForm(instance=item)

    if request.user != item.host:
        return HttpResponse('Your are not allowed here')


    if request.method == 'POST':
        form = RoomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/app/home")
    
    context = {"form": form}
    return render(request, "base/room_form.html", context)

@login_required(login_url="login")
def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect("/app/home")
    return render(request, "base/delete.html", {"obj": room})
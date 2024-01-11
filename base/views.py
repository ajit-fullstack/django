from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic
from .form import RoomForm
from django.db.models import Q


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
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
    context = {}
    return render(request, "base/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# Create your views here.
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
    context = {"room": room}
    return render(request, "base/room.html", context)


@login_required(login_url="/app/home")
def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/app/home")
        
    context = {"form": form}
    return render(request, "base/room_form.html", context)

def updateRoom(request, pk):
    item = Room.objects.get(id=pk)
    form = RoomForm(instance=item)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("/app/home")
    
    context = {"form": form}
    return render(request, "base/room_form.html", context)

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect("/app/home")
    return render(request, "base/delete.html", {"obj": room})
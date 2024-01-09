from django.shortcuts import render, redirect
from .models import Room, Topic
from .form import RoomForm

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    context = {"rooms": rooms, "topics": topics}
    return render(request, "base/home.html", context)

def room(request, pk):
    room = Room.objects.get(pk=pk)
    context = {"room": room}
    return render(request, "base/room.html", context)

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
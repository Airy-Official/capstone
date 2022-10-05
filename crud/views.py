from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student
from .models import Destination

# Create your views here.
def add(request):
    form = StudentForm(request.POST or None)
    # student = Student.objects.all()
    if form.is_valid():
        form.save()
    return render(request, 'add.html', {'form': form})

def show(request):
    student = Student.objects.all()
    return render(request, 'show.html', {'student': student})
    
def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, 'update.html', {'student':student})
    
def delete(request, id):
    form = Student.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect('/')

# def home(request):
#     return render(request, 'home.html', {})

def home(request):

    dest1 = Destination();
    dest1.name = 'Gingoog City'
    dest1.desc = 'The City of Goodluck'
    dest1.location = 'Central Mindanao University'
    dest1.img = 'hero-slider-1.jpg'
    dest1.price = '$69'

    dest2 = Destination();
    dest2.name = 'Pasig City'
    dest2.desc = 'The City of Goodluck'
    dest2.location = 'Central Mindanao University'
    dest2.img = 'hero-slider-2.jpg'
    dest2.price = '$69'

    dest3 = Destination();
    dest3.name = 'Cebu City'
    dest3.desc = 'The City of Goodluck'
    dest3.location = 'Central Mindanao University'
    dest3.img = 'hero-slider-3.jpg'
    dest3.price = '$69'

    dests = [dest1, dest2, dest3]

    return render(request, "home.html", {'dests': dests})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StartupForm
from .models import Startup
import requests
from decouple import config
import random

# Create your views here.
def home(request):
    context = {
    'title': 'Silly Startup Generator!',
    'startups': Startup.objects.order_by('-likes'),
    }
    return render(request, 'home.html', context)

@login_required()
def create(request):
    startup_form = StartupForm()
    if request.method == 'POST':
        startup_form = StartupForm(data=request.POST)
        if startup_form.is_valid():
            startup = startup_form.save(commit=False)
            startup.founder = request.user
            startup.save()
            return redirect('home')
        else:
            startup_form = StartupForm()


    return render(request, 'create.html', {
    'title': 'Make a startup',
    'startup_form':startup_form
    })

def get_photo(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    # API request
    ACCESS_KEY = config('ACCESS_KEY')
    response = requests.get('https://api.unsplash.com/photos/search/?client_id='+ ACCESS_KEY + '&query=puppies&page=1')
    unsplash_data = response.json()
   
    random_number = random.randint(0, (len(unsplash_data)- 1))
    print(unsplash_data[random_number]['urls'])
    photo_link = unsplash_data[random_number]['urls']['small']
    if request.method == 'POST':
        #Manually save all values from API Request
        print("Your request has been posted")
    return render(request, 'add_photo.html', {
        'title': 'oh my!',
        'startup': startup,
        'photo': photo_link

    })

def add_photo(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    # API request
    # ACCESS_KEY = config('ACCESS_KEY')
    # response = requests.get('https://api.unsplash.com/photos/search/?client_id='+ ACCESS_KEY + '&query=puppies&page=1')
    # unsplash_data = response.json()
   
    # random_number = random.randint(0, (len(unsplash_data)- 1))
    # print(unsplash_data[random_number]['urls'])
    # photo_link = unsplash_data[random_number]['urls']['small']
    if request.method == 'POST':
        #Manually save all values from API Request
        print("Your request has been posted")
    return render(request, 'add_photo.html', {
        'title': 'oh my!',
        'startup': startup,
        # 'photo': photo_link

    })


@login_required
def update(request,startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    update_startup_form = StartupForm(instance=startup)
    if request.method == 'POST':
        update_startup_form = StartupForm(request.POST, instance=startup)
        if update_startup_form.is_valid():
            update_startup_form.save()
            return redirect('profile', founder_id=request.user.id)
        else:
            update_startup_form = StartupForm(instance=startup)
    return render(request, 'update.html', {
            'title': 'Update {}'.format(startup.name),
            'update_startup_form': update_startup_form,
            'startup': startup,
            })

@login_required
def delete(request, startup_id):
    if request.method == 'POST':
        startup = get_object_or_404(Startup, pk=startup_id)
        startup.delete()
        return redirect('profile', founder_id=request.user.id)

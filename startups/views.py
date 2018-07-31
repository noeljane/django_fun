from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import StartupForm
from django.contrib import auth
from .models import Startup

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

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_startups = Startup.objects.filter(startup_id=user_id)
    context = {
    'title': 'Hello and welcome {}'.format(user.first_name),
    'user': user,
    'user_startups': user_startups
    }

    return render(request, 'profile.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StartupForm
from .models import Startup


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
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

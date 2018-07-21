from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StartupForm
from .models import Startup


# Create your views here.
def home(request):
    context = {
    'title':'Silly Startups',
    'startups': Startup.objects,
    }
    return render(request, 'home.html', context)

@login_required
def create(request):
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

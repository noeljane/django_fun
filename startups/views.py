from django.shortcuts import render
from .forms import StartupForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def create(request):
    startup_form = StartupForm()

    return render(request, 'create.html', {
    'title': 'Make a startup',
    'startup_form':startup_form
    })

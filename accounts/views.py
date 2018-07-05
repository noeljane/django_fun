from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.
def signup(request):
    signup_form = SignUpForm()
    context = {
    'title': 'Sign up!',
    'signup_form': signup_form
    }
    return render(request, 'signup.html', context)

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

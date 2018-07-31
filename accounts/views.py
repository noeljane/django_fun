from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import auth
from startups.models import Startup


# Create your views here.
def signup(request):
    registered = False
    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        signup_form = SignUpForm()
    context = {
    'title': 'Sign up!',
    'signup_form': signup_form,
    'registered': registered,
    }
    return render(request, 'signup.html', context)
#
#
# def auth_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username,password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             return render(request, 'login.html', {
#             'title': 'Something went wrong',
#             'error': 'Username or Password Invalid'
#             })
#
#     return render(request, 'login.html', {'title': 'Please Login'})
#
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

# @login_required
def profile(request, founder_id):
    founder = get_object_or_404(User, pk=founder_id)
    founder_startups = Startup.objects.filter(founder_id=founder_id)
    context = {
    'title': 'Hello and welcome {}'.format(founder.first_name),
    'founder': founder,
    'founder_startups': founder_startups
    }

    return render(request, 'profile.html', context)

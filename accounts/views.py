from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import auth


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


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username,password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
            'title': 'Something went wrong',
            'error': 'Username or Password Invalid'
            })

    return render(request, 'login.html', {'title': 'Please Login'})

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

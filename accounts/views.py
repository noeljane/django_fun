from django.shortcuts import render
from .forms import SignUpForm

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
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

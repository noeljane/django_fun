from django.forms import ModelForm
from .models import Startup

class StartupForm(ModelForm):
    class Meta():
        model = Startup
        fields = ['name', 'tagline', 'description' ]
        

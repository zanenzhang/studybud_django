from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants',]
        #Could also use a list of fields we want to render

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

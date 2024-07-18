from django import forms
from .models import Task 
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput)



class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline']

        
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','desc','deadline', 'status']

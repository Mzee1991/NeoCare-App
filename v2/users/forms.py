from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    group = forms.ChoiceField(
        choices=[("Doctors", "Doctors"), ("Nurses", "Nurses"), ("Lab Tech", "Lab Tech"), ("Admin", "Admin")],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nin_no = forms.CharField(
        max_length=100,
        initial='CMX10000000',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    contact = forms.CharField(
        max_length=100,
        initial='+256 ',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
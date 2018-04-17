from django.contrib.auth.models import User
from django import forms
from .models import Jela


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DodajRecept(forms.ModelForm):
    class Meta:
        model = Jela
        fields = ['ime', 'slika', 'kategorija', 'sastojci', 'sastojci_opis', 'nacin_pripreme', 'je_vegeterijansko']
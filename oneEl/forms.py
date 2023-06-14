from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
class AddOwn(forms.Form):
    name = forms.CharField(label="Name")
    package = forms.IntegerField(label="Number of package")
    modelgaika = forms.IntegerField(label="Type gaika")
    telef = forms.IntegerField(label="Telefon number")
    addres = forms.CharField(label="addres")

class FormForMod(forms.Form):
    link = forms.CharField(label="link")
    number = forms.IntegerField(label="number")





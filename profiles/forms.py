from django import forms

class FormProfile(forms.Form):
    image = forms.FileField()
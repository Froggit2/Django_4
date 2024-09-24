from django import forms

class RegForm(forms.Form):
    name = forms.CharField(max_length=30, label='name')
    password_1 = forms.CharField(label='password_1')
    password_2 = forms.CharField(label='password_2')
    age = forms.CharField(label='age')
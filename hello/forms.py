from django import forms
from .models import Friend


class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

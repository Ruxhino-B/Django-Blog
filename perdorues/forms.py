from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm




from .models import Perdorues

class PerdoruesCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Perdorues
        fields = ('username','email','mosha')




class PerdoruesChangeForm(UserChangeForm):
    class Meta:
        model = Perdorues
        fields = ('username','email','mosha')

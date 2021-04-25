from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import PerdoruesCreationForm

# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = PerdoruesCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


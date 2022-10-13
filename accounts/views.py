from django.shortcuts import render
from django.views import generic
from . import forms
from django.urls import reverse_lazy
# Create your views here.

class SignUpPage(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'
    
    
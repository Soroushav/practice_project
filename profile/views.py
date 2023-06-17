from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.html'


class ProfilePageView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user'


class CreateUserView(CreateView):
    template_name = 'account/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')

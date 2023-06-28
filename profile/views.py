from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib import messages
from .email import create_user_sent_email


class UserActionMixin:

    @property
    def success_msg(self):
        return NotImplemented

    @property
    def error_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, self.error_msg)
        return super().form_invalid(form)


class CreateUserMixin:
    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

class HomePageView(TemplateView):
    template_name = 'home.html'


class ProfilePageView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user'


class EditUserView(UserActionMixin, UpdateView):
    model = get_user_model()
    template_name = 'profile_edit.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')


class SearchUserView(ListView):
    template_name = 'profile_search.html'
    model = get_user_model()
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            return queryset.filter(username__icontains=q)
        return queryset


class CreateUserView(UserActionMixin, CreateUserMixin, CreateView):
    template_name = 'account/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    success_msg = "Created"
    error_msg = "User did not created"
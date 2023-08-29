from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    """

    """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    """

    """
    model = User
    form_class = UserProfileForm
    # template_name = 'users/register.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        """
        Позволяет делать необязательным передачу pk объекта
        """
        return self.request.user

    # def __init__(self, *args, **kwargs):
    #     """
    #     Позволяет не выводить в профиле поле пароля
    #     """
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].widget = forms.HiddenInput()

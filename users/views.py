from django.http import request
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView, UpdateView
from .models import User
from .forms import LoginForm, UserCreationForm, UserChangeForm, UserUpdateForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/update.html'

    def form_valid(self, form):
        messages.success(self.request, "登録しました")
        return super().form_valid(form)



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"

def get_queryset(self):
        return User.objects.get(id=self.request.user.id)




class Logout(LogoutView):
    template_name = 'mysite/home.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'


class UserUpdateView(LoginRequiredMixin, OnlyYouMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/signup.html'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "登録しました")
        return super().form_valid(form)

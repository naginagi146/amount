from django.shortcuts import render
from django.views.generic import CreateView, DetailView, TemplateView
from .models import User
from .forms import LoginForm, UserCreationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
    template_name = 'users/signup.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        return reverse('mysite/login')


class ProfileView(OnlyYouMixin, DetailView):
    model = User
    template_name = "users/profile.html"




class Logout(LogoutView):
    template_name = 'mysite/home.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
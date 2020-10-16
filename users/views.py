from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from .models import User
from accounts.models import Item
from .forms import LoginForm, UserCreationForm, UserUpdateForm
from django.urls import reverse_lazy
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
    template_name = 'users/signup.html'

    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        return reverse_lazy('users/profile', kwargs={'pk': self.object.pk})


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "users/profile.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_item"] = Item.objects.filter(contributor_id=self.kwargs['pk'])
        return context

class UserUpdateView(OnlyYouMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/update.html'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        result = super().form_valid(form)
        return result

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})

class Logout(LogoutView):
    template_name = 'mysite/home.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
from django.shortcuts import render
from django.views.generic import CreateView
from .models import User
from .forms import UserCreationForm
from django.urls import reverse

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
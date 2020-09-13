from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('users/create/', views.UserCreateView.as_view(), name='users_create'),
]
from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='users_create'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
]
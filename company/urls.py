from django.urls import path
from . import views

app_name = 'company'


urlpatterns = [
    path('', views.CompanyListView.as_view(), name='companylist'),
    path('<int:pk>/', views.CompanyDetailView.as_view(), name='companydetail')
]

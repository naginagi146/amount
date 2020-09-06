from django.urls import path
from . import views

app_name = 'company'


urlpatterns = [
    path('company/list', views.CompanyListView.as_view(), name='companylist'),
    path('company/detail/<int:pk>/', views.CompanyDetailView.as_view(), name='companydetail'),
    path('reply/create', views.ReplyCreateView.as_view(), name='replycreate'),
    path('company/update/<int:pk>/', views.ReplyUpdateView.as_view(), name='companyupdate'),
    path('company/delete/', views.ReplyDeleteView.as_view(), name='companydelete'),
]

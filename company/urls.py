from django.urls import path
from . import views

app_name = 'company'


urlpatterns = [
    # path('company/item/list/', views.CompanyListView.as_view(), name='company_list'),
    # path('company/item/detail/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('reply/create/<int:pk>/', views.ReplyCreateView.as_view(), name='reply_create'),
    path('company/reply/update/<int:pk>/', views.ReplyUpdateView.as_view(), name='company_update'),
    path('company/reply/delete/', views.ReplyDeleteView.as_view(), name='company_delete'),
]

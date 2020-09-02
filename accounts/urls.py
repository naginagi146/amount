from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.item_list, name='item_list'),
    # path('', ItemCreateView.as_view()),
    path('', views.ItemListView.as_view(), name='home'),
    path('', views.ItemCreateView.as_view(), name='item_create')
]

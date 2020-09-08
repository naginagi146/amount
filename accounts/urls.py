from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('accounts/item/list/', views.ItemListView.as_view(), name='item_list'),
    path('accounts/item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('accounts/item/detail/', views.ItemDetailView.as_view(), name='item_detail'),
    path('accounts/item/update/', views.ItemUpdateView.as_view(), name='item_update'),
    path('accounts/item/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]

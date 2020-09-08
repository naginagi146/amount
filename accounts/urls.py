from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('itemlist/', views.ItemListView.as_view(), name='item_list'),
    path('itemcreate/', views.ItemCreateView.as_view(), name='item_create'),
    path('itemdetail/', views.ItemDetailView.as_view(), name='item_detail'),
    path('itemupdate/', views.ItemUpdateView.as_view(), name='item_update'),
    path('itemdelete/', views.ItemDeleteView.as_view(), name='item_delete'),
]

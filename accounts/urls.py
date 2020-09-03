from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.ItemListView.as_view(), name='home'),
    path('', views.ItemCreateView.as_view(), name='item_create'),
    path('', views.ItemDetailView.as_view(), name='item_detail'),
    path('', views.ItemUpdateView.as_view(), name='item_update'),
    path('', views.ItemDeleteView.as_view(), name='item_delete'),
]

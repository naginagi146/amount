from django.urls import path
from .views import ItemCreateView
from django.conf.urls import url


urlpatterns = [
    # path('', views.item_list, name='item_list'),
    # path('', ItemCreateView.as_view()),
    url(r'^create$', ItemCreateView.as_view()),
]

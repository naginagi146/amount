from company.models import Reply
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from accounts.models import Item
from django.urls import reverse_lazy

class CompanyListView(ListView):
    model = Item
    queryset = Item.objects.all()
    context_object_name = 'item_listquery'
    template_name = "company_list.html"
    paginate_by = 5

class CompanyDetailView(DetailView):
    model = Item
    template_name = "company_detail.html"


class CompanyCreateView(CreateView):
    model = Reply
    template_name = "company_create.html"
    fields = ['user', 'price', 'text']
    success_url = reverse_lazy('companylist')

class CompanyUpdateView(UpdateView):
    model = Reply
    template_name = "company_update.html"
    fields = ['user', 'price', 'text']
    success_url = reverse_lazy('companylist')





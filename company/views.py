from company.forms import ReplyCreateForm
from django.contrib import messages
from company.models import Reply
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from accounts.models import Item
from django.urls import reverse_lazy

class CompanyListView(ListView):
    model = Item
    queryset = Item.objects.all()
    context_object_name = 'item_listquery'
    template_name = "company/company_list.html"
    paginate_by = 5

class CompanyDetailView(DetailView):
    model = Item
    template_name = "comapny/company_detail.html"


class ReplyCreateView(CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = "company/reply_create.html"
    fields = ['user', 'price', 'text']
    success_url = reverse_lazy('companylist')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を返信しました'.format(form.instance))
        return result

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView).get_context_data(**kwargs)
        context["Item"] = self.kwargs['Item']
        return context


class ReplyUpdateView(UpdateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = "company/reply_update.html"
    fields = ['user', 'price', 'text']
    success_url = reverse_lazy('companylist')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView).get_context_data(**kwargs)
        context["Item"] = self.kwargs['Item']
        return context

class ReplyDeleteView(DeleteView):
    template_name = 'company/reply_delete.html'
    model = Reply

    success_url = reverse_lazy('companylist')

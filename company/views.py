from company.forms import ReplyCreateForm
from django.contrib import messages
from company.models import Reply
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from accounts.models import Item
from django.urls import reverse_lazy
from django.db.models import Q

class CompanyListView(ListView):
    model = Item
    queryset = Item.objects.all()
    context_object_name = 'products'
    template_name = "company/company_list.html"
    paginate_by = 10


    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Item.objects.filter(
                Q(name__icontains=q_word) | Q(item_model__icontains=q_word) | Q(category__icontains=q_word))
        else:
            object_list = Item.objects.all()
        return object_list

class UserItemListView(ListView):
    model = Item
    context_object_name = 'user_items'
    template_name = "company/user_item.html"
    paginate_by = 10

    def get_queryset(self):
        return Item.objects.filter()
    # ↑ユーザーごとのアイテムリスト表示

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

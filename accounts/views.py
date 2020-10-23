from django.db.models import query
from django.db.models.query import QuerySet
from company.models import Reply
from users.models import User
from users.views import OnlyYouMixin
from django.http import request
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ItemCreateForm, ImageFormset
from .models import Item, Image
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import HttpResponseRedirect
from .notify import send_notification




class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "accounts/item_list.html"
    context_object_name = 'items'
    paginate_by = 10
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_list = []
        item = Item.objects.values('id','images')
        item_list.append(item)
        all_items = Item.objects.all()
        for item in all_items:
            print(item)
            image_list = Image.objects.filter(target_id=item)
            context["images"] = item_list
            print(context)
            return context


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     item_id = {}
    #     item_list = []
    #     images = 'target_id'
    #     item_id['id'] = images
    #     item_id = Item.objects.values('id')
    #     item_list.append(item_id)
    #     all_item = Item.objects.all()
    #     # print(item_list)→ここでitemList in dictのクエリが一つできる
    #     for item in all_item:
    #         images = {}
    #         images = Image.objects.filter(target_id=item_id).values()
    #         item_list.append(images)
    #         context["images"] = images
    #         print(item_list)
    #     return context

        #     images ={}
        #     image_list = []
        #     images = Image.objects.filter(target_id=item_id)
        #     image_list.append(images)
        #     item_list.append(images)
        #     context["images"] = images
        #     print(item_list)
        # return context
        # ↑リストはまとめられたが、全オブジェクトでまとまってる



        # item_list = Item.objects.values('id')
        # for item_list in Image.objects.select_related('target').filter(target_id__in=item_list)
        # context["images"] = Image.objects.filter(target_id__in=item_list)
        # context["images"] = Image.objects.select_related('target').filter(target_id__in=item_list)
        # return context


    def get_queryset(self):
        current_user = self.request.user
        q_word = self.request.GET.get('query')
        if current_user.is_customer:
            return Item.objects.filter(contributor_id=current_user.id)
        elif q_word:
            object_list = Item.objects.filter(
                Q(name__icontains=q_word) | Q(category__icontains=q_word) | Q(contributor__user_name__icontains=q_word))
            return object_list
        else:
            return Item.objects.all()

    # def get_queryset(self):
    #     q_word = self.request.GET.get('query')

    #     if q_word:
    #         object_list = Item.objects.filter(
    #             Q(name__icontains=q_word) | Q(category__icontains=q_word) | Q(contributor__user_name__icontains=q_word))
    #     else:
    #         object_list = Item.objects.all()
    #     return object_list

class UserItemListView(ListView):
    model = Item
    template_name = "accounts/user_item_list.html"
    context_object_name = 'user_item'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return Item.objects.filter(user=self.request.user)
    # 表示されねえ・・・forループの書き方？

    # def get_context_data(self, **kwargs):
    #     user = self.request.user
    #     context = super().get_context_data(**kwargs)
    #     context["items"] = user.item_set.all().order_by('-created_at')
    #     return context


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "accounts/item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["replys"] = Reply.objects.filter(target_id=self.kwargs['pk'])
        return context



class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemCreateForm
    formset = ImageFormset
    template_name = "accounts/item_create.html"


    def get_context_data(self, **kwargs):
        data = super(ItemCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ImageFormset(self.request.POST, self.request.FILES)
        else:
            data['formset'] = ImageFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['formset']

        if image_formset.is_valid():
            with transaction.atomic():
                image_formset.instance = self.object
                image_formset.save()
                self.object = form.save()
                send_notification(self.object, '登録')

        return super(ItemCreateView, self).form_valid(image_formset)

    def get_success_url(self):
        return reverse_lazy('accounts:item_list')

class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemCreateForm
    formset = ImageFormset
    template_name = "accounts/item_update.html"

    def get_context_data(self, **kwargs):
        data = super(ItemUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ImageFormset(self.request.POST, self.request.FILES)
        else:
            data['formset'] = ImageFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_formset = context['formset']

        if image_formset.is_valid():
            with transaction.atomic():
                image_formset.instance = self.object
                image_formset.save()
                self.object = form.save()

        return super(ItemUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:item_detail',  kwargs={'pk': self.object.pk})

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/item_delete.html'
    model = Item

    success_url = reverse_lazy('accounts:item_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, '「{}」を削除しました'.format(self.object))
        return result


# def item_list(request):
#     form = ItemCreateForm(request.POST or None)
#     context = {'form': form}
#     if request.method == 'POST' and form.is_valid():
#         post = form.save(commit=False)
#         image_formset = ImageFormset(request.POST, files=request.FILES, instance=post)  # 増えた
#         if  image_formset.is_valid():
#             post.save()
#             image_formset.save()
#             return redirect('accounts:index')

#         # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
#         else:
#             context['image_formset'] = image_formset

#     # GETのとき
#     else:
#         # 空のformsetをテンプレートへ渡す
#         context['image_formset'] = ImageFormset()  # 増えた

#     return render(request, 'accounts/item_list.html', context)

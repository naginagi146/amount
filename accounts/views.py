from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ItemCreateForm, ImageFormset
from .models import Item, Image
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    queryset = Item.objects.all()
    template_name = "accounts/item_list.html"
    context_object_name = 'items'
    paginate_by = 5
    ordering = ['-created_at']

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Item.objects.filter(
                Q(name__icontains=q_word) | Q(item_model__icontains=q_word) | Q(category__icontains=q_word))
        else:
            object_list = Item.objects.all()
        return object_list


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "accounts/item_detail.html"


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item, Image
    fields = ['__all__']
    form_class = ItemCreateForm, ImageFormset
    template_name = "accounts/item_create.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を作成しました'.format(form.instance))
        return result


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemCreateForm, ImageFormset
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '「{}」を更新しました'.format(form.instance))
        return result

class ItemDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'accounts/item_delete.html'
    model = Item

    success_url = reverse_lazy('index')



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

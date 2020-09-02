from django.shortcuts import render
from django.contrib import messages
from .forms import ItemCreateForm, ImageFormset
from .models import Item, Image
from django.views.generic import CreateView, ListView



class ItemListView(ListView):
    model = Item, Image
    template_name = "accounts/index.html"
    context_object_name = 'Item'
    paginate_by = 5



class ItemCreateView(CreateView):
    model = Item, Image
    fields = ['__all__']
    form_class = ItemCreateForm, ImageFormset
    template_name = "accounts/item_list.html"
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, "完了しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, "完了できませんでした")
        return super().form_invalid(form)


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

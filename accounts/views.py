from django.shortcuts import render
from .forms import ItemCreateForm,ImageFormset

def item_list(request):
    form = ItemCreateForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        image_formset = ImageFormset(request.POST, files=request.FILES, instance=post)  # 増えた
        if  image_formset.is_valid():
            post.save()
            image_formset.save()
            return redirect('app:index')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['image_formset'] = image_formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['image_formset'] = ImageFormset()  # 増えた

    return render(request, 'accounts/item_list.html', context)
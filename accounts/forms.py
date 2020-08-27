# from django import forms
# from .models import Post

# #以下モデルのプルダウンメニュー用フォーム
# class PostCreateForm(forms.ModelForm):
#     Category = forms.ModelChoiceField(
#         label='アイテムタイプ',
#     )
#     Conditon = forms.ModelChoiceField(
#         label='状態ランク',
#     )
#     class Meta:
#         model = Post

# # class ConditionCreateForm(forms.ModelForm):
# #     Conditon = forms.ModelChoiceField(
# #         label='状態ランク',
# #         queryset=Condition.objects,
# #         required=False
# #     )

#     field_order = ('brand', 'item_model', 'category','condition',)
from django import forms
from .models import Category,Condition

#以下モデルのプルダウンメニュー用フォーム
class CategoryCreateForm(forms.ModelForm):
    Category = forms.ModelChoiceField(
        label='アイテムタイプ',
        queryset=Category.objects,
        required=False
    )

class ConditionCreateForm(forms.ModelForm):
    Conditon = forms.ModelChoiceField(
        label='状態ランク',
        queryset=Condition.objects,
        required=False
    )

    field_order = ('brand', 'item_model', 'category','condition',)
from django import forms
from .models import Item, Image


class ItemCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Item
        fields = '__all__'


ImageFormset = forms.inlineformset_factory(
    Item, Image, fields='__all__',
    extra=5,
)

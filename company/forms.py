from django import forms
from .models import Reply

class ReplyCreateForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ( "price", "text")


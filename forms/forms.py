from django import forms
from .models import SubscribedUser


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribedUser
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editContent', 'placeholder':'Ваш email..'})
        }
        labels = {
            'email':''
        }

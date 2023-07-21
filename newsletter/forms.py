from django import forms
from django.core.mail import send_mail

from .models import SubscribedUsers

class SubscribeForm(forms.ModelForm):

    class Meta:
        model=SubscribedUsers
        fields= ('email',)
        # widgets = {
        #     'email': forms.TextInput(attrs={'class':'editContent', 'placeholder':'Ваш Email...'})
        # }
        # labels = {
        #     'email': ''
        # }

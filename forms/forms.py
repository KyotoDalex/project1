from django import forms
from snippets import snippets


class CatsForm(forms.Form):
    category = snippets.NewsCategory
    choice_field = forms.ChoiceField(choices=category)
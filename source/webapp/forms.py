from django import forms
from django.forms import widgets




class ReviewForm(forms.Form):
    author = forms.CharField(max_length=40, required=True, label='Автор')
    email = forms.EmailField(max_length=200, required=True, label='Почта')
    text = forms.CharField(max_length=3000, required=True, label='Текст',
                           widget=widgets.Textarea)
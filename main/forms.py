from dataclasses import fields
from tkinter.ttk import Widget
from .models import Article
from django.forms import ModelForm, TextInput, Textarea

class ArticleForm(ModelForm):
  class Meta:
    model = Article
    fields = ['title', 'text']
    widgets = {
      'title': TextInput(attrs = {
        'class': 'form-control mb-4',
        'placeholder': 'Enter the title',
      }),
      'text': Textarea(attrs = {
        'class': 'form-control mb-4',
        'placeholder': 'Enter the text',
        'rows': '4',
      })
      }
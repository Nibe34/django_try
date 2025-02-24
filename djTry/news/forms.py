from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'News title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Anons'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date'
            })
        }
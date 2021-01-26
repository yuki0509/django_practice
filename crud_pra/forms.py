from django import forms
from . models import Article, Book

class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ['title', 'content', 'pub_date']

class BookForm(forms.ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'image']

# class SearchForm(forms.Form):
#   key_word = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'検索キーワード'}))

from django import forms
from webapp.models import User

class UserSearchForm(forms.Form):
    user_name = forms.CharField(max_length=200, required=False, label='Имя пользователя')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'favorites', 'description']

class ArticleSearchForm(forms.Form):
    article_title = forms.CharField(max_length=200, required=False, label='Ключевые слова')

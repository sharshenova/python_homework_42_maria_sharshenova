from django import forms
from webapp.models import User, Article, Comment

class UserSearchForm(forms.Form):
    user_name = forms.CharField(max_length=200, required=False, label='Имя пользователя')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'favorites', 'description']

class ArticleSearchForm(forms.Form):
    article_keywords = forms.CharField(max_length=200, required=False, label='Ключевые слова')

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['parent_comment', 'text', 'article', 'commented_by']

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
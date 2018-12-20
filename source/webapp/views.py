from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from webapp.models import User, Article, Comment, Rating
from webapp.forms import UserSearchForm, ArticleSearchForm, UserForm, ArticleForm, CommentForm
from django.urls import reverse, reverse_lazy



class UserListView(ListView, FormView):
    model = User
    template_name = 'user_list.html'
    form_class = UserSearchForm

    def get_queryset(self):
        user_name = self.request.GET.get('user_name')
        if user_name:
            return self.model.objects.filter(name__icontains=user_name)
        else:
            return self.model.objects.all()


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


# class ArticleListView(ListView, FormView):
#     def __init__(self):
#         self.articles = []
#
#     model = Article
#     template_name = 'article_list.html'
#     form_class = ArticleSearchForm
#
#     def get_queryset(self):
#
#         article_keywords = self.request.GET.get('article_keywords')
#         if article_keywords:
#             self.articles += self.model.objects.filter(title__icontains=article_keywords)
#             self.articles += self.model.objects.filter(text__icontains=article_keywords)
#             return self.articles
#
#         else:
#             return self.model.objects.all()


class ArticleListView(ListView, FormView):

    model = Article
    template_name = 'article_list.html'
    form_class = ArticleSearchForm

    def get_queryset(self):

        article_title = self.request.GET.get('article_title')
        if article_title:
            return self.model.objects.filter(title__icontains=article_title)
        else:
            return self.model.objects.all()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class UserFavoritesView(DetailView):
    model = User
    template_name = 'user_favorites.html'


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_update.html'
    form_class = ArticleForm
    success_url = reverse_lazy('article_list')


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'comment_create.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article_detail', kwargs={'pk': self.object.article.pk})
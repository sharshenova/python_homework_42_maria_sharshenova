from django.contrib import admin
from django.urls import path
from webapp.views import UserListView, UserDetailView, ArticleListView, ArticleDetailView, UserFavoritesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('users', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('favorites/<int:pk>', UserFavoritesView.as_view(), name='user_favorites'),
]
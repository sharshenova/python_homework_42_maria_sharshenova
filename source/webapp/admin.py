from django.contrib import admin
from webapp.models import User, Article, Comment, Rating


admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Rating)
from django.db import models
from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    favorites = models.ManyToManyField('Article', blank=True, related_name='favored_by', verbose_name='Избранное')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=4000, verbose_name='Текст статьи')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='articles', verbose_name='Автор')

    def __str__(self):
        return self.title

    def root_comments(self):
        return self.comments.filter(parent_comment__isnull=True)


class Comment(models.Model):
    parent_comment = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.PROTECT, related_name='comments', verbose_name='Родительский комментарий')
    text = models.TextField(max_length=1000, verbose_name='Текст комментария')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='comments', verbose_name='Статья')
    commented_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comments', verbose_name='Автор')
    datetime = models.DateTimeField(default=datetime.now, verbose_name='Дата')

    def __str__(self):
        return self.text


class Rating(models.Model):
    RATING_VERY_BAD = 'very_bad'
    RATING_BAD = 'bad'
    RATING_MIDDLING = 'middling'
    RATING_WELL = 'well'
    RATING_EXCELLENT = 'excellent'

    RATING_CHOICES = (
        (RATING_VERY_BAD, 'Очень плохо'),
        (RATING_BAD, 'Плохо'),
        (RATING_MIDDLING, 'Средне'),
        (RATING_WELL, 'Хорошо'),
        (RATING_EXCELLENT, 'Отлично')
    )

    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='ratings', verbose_name='Статья')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ratings', verbose_name='Рецензент')
    value = models.CharField(max_length=20, choices=RATING_CHOICES, verbose_name='Оценка')

    def __str__(self):
        return self.get_value_display()

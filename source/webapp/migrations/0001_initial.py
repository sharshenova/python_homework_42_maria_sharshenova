# Generated by Django 2.1 on 2018-12-16 11:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=4000, verbose_name='Текст статьи')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст комментария')),
                ('datetime', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата написания комментария')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_comments', to='webapp.Article', verbose_name='Статья с комментарием')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя пользователя')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favored_by', to='webapp.Article', verbose_name='Избранное')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='commented_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments_by', to='webapp.User', verbose_name='Автор комментария'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comments', to='webapp.Comment', verbose_name='Корневой комментарий'),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='webapp.User', verbose_name='Автор'),
        ),
    ]

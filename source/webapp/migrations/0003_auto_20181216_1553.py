# Generated by Django 2.1 on 2018-12-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181216_1221'),
    ]

    operations = [
        migrations.RenameField('comment', 'article_id', 'article')
    ]

# Generated by Django 4.1.7 on 2023-03-29 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='phvid',
        ),
    ]
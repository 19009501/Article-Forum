# Generated by Django 4.1.7 on 2023-04-01 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0006_alter_article_forkey_alter_article_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set(),
        ),
    ]
# Generated by Django 4.1.7 on 2023-04-01 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ArticleApp', '0011_alter_subcomment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArticleApp.article'),
        ),
    ]

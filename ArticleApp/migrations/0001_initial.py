# Generated by Django 4.1.7 on 2023-03-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('phvid', models.ImageField(upload_to=None)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

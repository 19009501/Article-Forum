from django.db import models
from ArticleApp.models import Article,Login
from django.contrib.auth.models import User

class Like(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    
# Create your models here.

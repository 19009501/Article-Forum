from django.db import models

from rest_framework import serializers
import string
class Signup(models.Model):
    name=models.CharField(max_length=20,default=None)
    email=models.EmailField(max_length=30,default=None)
    phone_number=models.CharField(max_length=15,null=False)
    password=models.CharField(max_length=10,default=None,null=True)
    
class Login(models.Model):

    username=models.OneToOneField(Signup,on_delete=models.CASCADE,null=True)
    email=models.EmailField(null=True)
    password=models.CharField(max_length=15,null=False)
    date=models.DateTimeField(auto_now_add=True)   
class Article(models.Model):
    
    forkey=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=80)
    content=models.TextField()
    #phvid=models.ImageField(upload_to=None,height_field=None, width_field=None, max_length=100)
    date=models.DateTimeField(auto_now=True)
    class Meta:

        unique_together = ("forkey", "title")


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    time=models.DateTimeField(auto_now_add=True)
    comm=models.TextField()
class Subcomment(models.Model):

    article=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    time=models.DateTimeField(auto_now_add=True)
    comm=models.TextField()
    commentrep=models.ForeignKey(Comment,models.CASCADE,null=True)


# Create your models here.

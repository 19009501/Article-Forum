from django.contrib import admin
from ArticleApp.models import *
from likeApp.models import *
@admin.register(Article,Like,Login,Comment,Subcomment,Signup)
class AuthorAdmin(admin.ModelAdmin):
    pass
# Register your models here.

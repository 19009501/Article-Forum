"""forumArticles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ArticleApp.views import ArticleViewSet,LikeViewSet ,LoginViewSet,CommentViewSet,SubcommentViewset,SignupViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router=DefaultRouter()
router.register(r'article',ArticleViewSet,basename="show articles") 
router.register(r'likes',LikeViewSet,basename="showlikes")
router.register(r'login',LoginViewSet,basename="login")
router.register(r'comments',CommentViewSet,basename="article_comments")
router.register(r'replies',SubcommentViewset,basename="comment_reply")
router.register(r'signup',SignupViewSet,"user signing")
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

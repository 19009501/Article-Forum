from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import status
from rest_framework.response import Response
from ArticleApp.models import Article,Login,Comment,Subcomment,Signup
from likeApp.models import Like
from .serializers import ArticleSerializer,LikeSerializer,CommentSerializer,SubcommentSerializer,SignupSerializer
from rest_framework.decorators import action

from ArticleApp.models import Login
from rest_framework.authtoken.models import Token

# user =Login.objects.get(username=)
# token = Token.objects.create(user=Login)
# print(token.key)

 
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class to allow only the owner of an article to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
class LoginViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, AllowAny]  # fixed

    queryset = Login.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):  # fixed
        serializer = LoginSerializer(data=request.data)
        data=request.data
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # serializer.is_valid(raise_exception=True)
        # instance = serializer.save()
        # check=Login.objects.filter(username=request.username)
        # print(check)
        # user = Login.objects.get(check,username=request.username)
        # refresh = RefreshToken.for_user(user)
        # return Response({'data': serializer.data,
        #                  'refresh': str(refresh),
        #                  'access': str(refresh.access_token)})
    

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    def list(self, request, *args, **kwargs):
        print("list")
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    def create(self, request,*args, **kwargs):
        #data = Article.objects.filter(forkey)
        article = Article()
        article.save()
        forkey=Login()
        serializer = self.get_serializer(data=request.data)
        data=request.data
        print("article posted")
        if data.get('forkey') is None:
            return Response(
                {"status": 400, 'message': 'not logged in'}
            )
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, pk=None):
        print("deleted")
        try:
            article = self.queryset.get(pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
from django.shortcuts import get_object_or_404
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        article = self.get_object()
        Like.objects.create(user=request.user, article=article)
        return Response({'status': 'liked'})
    def list(self, request):
        likes = self.get_queryset()
        serializer = self.get_serializer(likes, many=True)
        return Response(serializer.data)
class CommentViewSet(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
class SubcommentViewset(viewsets.ModelViewSet):
    queryset=Subcomment.objects.all()
    serializer_class=SubcommentSerializer

class SignupViewSet(viewsets.ViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

    def create(self, request):
        print("user created")
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def list(self,request):
        print("user list")
        queryset=Signup.objects.all()
        serializer=SignupSerializer(queryset,many=True)
        return Response(serializer.data)
    def destroy(self,request,pk=None):
        print("user removed")
        try:
            user= self.queryset.get(pk=pk)
        except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def update(self, request, pk,*args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.queryset.get(pk=pk)
        serializer = SignupSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    # class SignupViewSet(viewsets.ModelViewSet):
    #       queryset = Signup.objects.all()
    #       serializer_class = SignupSerializer

    # def get_object(self):
    #     queryset = Signup.objects.all()
    #     obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
    #     return obj

    #

    
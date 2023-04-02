from rest_framework import serializers
from ArticleApp.models import Article,Login,Comment,Subcomment,Signup
from likeApp.models import Like
class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Article
        fields=['id','title','content','date','forkey']

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Article
        fields=['id','title','content','date','forkey']
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = ['user','article']

class SubcommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Subcomment
        fields=['commentrep']
class CommentSerializer(serializers.ModelSerializer):
    commentrep=SubcommentSerializer(read_only=True,many=True)
    class Meta:
        model=Comment
        fields=['user','comm','article','commentrep']
class LoginSerializer(serializers.ModelSerializer):
    forkey=ArticleSerializer(read_only=True,many=True)
    article=LikeSerializer(read_only=True,many=True)
    article=CommentSerializer(read_only=True,many=True)
    commentrep=SubcommentSerializer(read_only=True,many=True)
    class Meta:
        
        model=Login
        fields="__all__"
class SignupSerializer(serializers.ModelSerializer):
    username=LoginSerializer(read_only=True,many=True)
    class Meta:
        model = Signup
        fields = ['name','email',"phone_number",'password','username']
    # def validate(self,value):
    #     queryset=Signup.objects.get()
        
    #     if value['name'].isalpha() or queryset.phone_number!="91"+value['phone_number']:
    #        raise serializers.ValidationError("field must contain alphabates/number start with 91")
    #     return value
from enum import auto
from api.models import Articles, Comments
from rest_framework import serializers
import uuid
# from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Articles
        fields = ['article_id','owner','article_title','description','updated_at', 'total_likes','total_comments']
    

# class UserSerializer(serializers.ModelSerializer):
#     id=serializers.UUIDField(default=uuid.uuid4)
#     first_name=serializers.CharField(max_length=50)
#     last_name=serializers.CharField(max_length=50)
#     # username=serializers.CharField(max_length=20,unique=True)
#     email=serializers.CharField(max_length=150)
#     is_active=serializers.BooleanField(default=True)
#     is_admin=serializers.BooleanField(default=False)
#     is_writer=serializers.BooleanField(default=False)
#     is_editor=serializers.BooleanField(default=False)
#     last_login=serializers.DateTimeField()
#     # created_at = serializers.DateTimeField()
#     # updated_at=serializers.DateTimeField()  

#     class Meta:
#         model = User
#         fields = ['id', 'username','first_name','last_name','email','is_active','is_admin','is_writer','is_editor','last_login']

#     def validate(self, attrs):
#         if User.objects.filter(email=attrs['email']).exists():
#             raise serializers.ValidationError(
#                 {'email',('Email is already in use')})
#         return super().validate(attrs)

#     def create(self, validated_data):
#         return User.username


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment_id', 'comment','updated_at']

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = Profile.objects.create_user(validated_data['first_name'],validated_data['last_name'],validated_data['username'], validated_data['email'], validated_data['password'])

#         return user
     
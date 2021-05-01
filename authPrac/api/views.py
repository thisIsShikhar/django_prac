from django_filters.filters import OrderingFilter
from rest_framework import generics
from rest_framework.serializers import Serializer
from api import serializers
from django.contrib.auth.models import User
from api.models import Articles, Comments, Likes, Media

from rest_framework import generics, permissions,status
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# from .serializers import UserSerializer

from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer

from rest_framework.pagination import (

    LimitOffsetPagination,
    PageNumberPagination
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


class ArticlesList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class=LimitOffsetPagination

    filter_backends=[OrderingFilter,DjangoFilterBackend]
    ordering_fields=['total_likes']
    filterset_fields=['is_featured']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer


class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer

class LikesList(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Likes.objects.all()
    serializer_class = serializers.PostSerializer

class MediaList(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = serializers.PostSerializer

# Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         # "token": AuthToken.objects.create(user)[1]
#         })


# class RegisterView(GenericAPIView):
#     serializer_class=UserSerializer

#     def post(self,request):
#         serializer=UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


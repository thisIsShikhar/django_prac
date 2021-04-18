from django_filters.filters import OrderingFilter
from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from api.models import Articles

from rest_framework.pagination import (

    LimitOffsetPagination,
    PageNumberPagination
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


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
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer

class LikesList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer

class MediaList(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class MediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.PostSerializer
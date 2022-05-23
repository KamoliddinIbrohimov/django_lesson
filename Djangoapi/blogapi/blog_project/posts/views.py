from django.shortcuts import render
from .serializers import PostSerializers, UserSerializer
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from .models import Post
from django.contrib.auth import get_user_model


# Create your views here.


# class PostList(ListCreateAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializers
#
#
# class UserList(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
class PostViewSet(ModelViewSet):
    # parser_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers
class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
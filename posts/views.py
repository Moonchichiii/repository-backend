from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'content', 'user__username']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


from django.db.models import Count
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer, PostListSerializer
from backend.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    # handles CRUD operations for posts
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['title', 'content', 'user__username']
    ordering_fields = ['likes_count', 'comments_count', 'likes__created_at']

    
    def perform_create(self, serializer):
        # links the current loggedin user with new posts
        serializer.save(user=self.request.user)


    def get_serializer_class(self):
        # serializer based on user authentication and action
        if self.action == 'list' and not self.request.user.is_authenticated:
            return PostListSerializer
        return PostSerializer

    def get_queryset(self):
        # fetches posts based on likes and comments count; full content not readable for unauthenticated users
        queryset = Post.objects.all().annotate(
            likes_count=Count('likes', distinct=True),
            comments_count=Count('comments', distinct=True)
        ).order_by('-created_at')
        if not self.request.user.is_authenticated:
            queryset = queryset.defer('content') 
        return queryset
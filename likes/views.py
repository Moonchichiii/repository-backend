from rest_framework import viewsets, permissions
from backend.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

        
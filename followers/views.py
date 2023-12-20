from rest_framework import viewsets, permissions
from .models import Follower
from .serializers import FollowerSerializer
from backend.permissions import IsOwnerOrReadOnly



class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

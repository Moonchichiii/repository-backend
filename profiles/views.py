from rest_framework import viewsets
from .models import Profile
from .serializers import UserProfileSerializer
from backend.permissions import IsOwnerOrReadOnly 

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):        
        return super().get_queryset()
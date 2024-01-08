from rest_framework import viewsets
from .models import Profile
from .serializers import UserProfileSerializer
from backend.permissions import IsOwnerOrReadOnly 

from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated



# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    

    def get_queryset(self):        
        return super().get_queryset()


class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile_image_url = request.data.get("image_url")
        
        if profile_image_url:
            profile.profile_image = profile_image_url
            profile.save()
        
        return Response({ "message": "Profile updated"})
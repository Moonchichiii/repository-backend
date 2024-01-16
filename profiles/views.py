from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from backend.permissions import IsOwnerOrReadOnly 

from .models import Profile

from .serializers import UserProfileSerializer


# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, user=self.request.user)
        self.check_object_permissions(self.request, obj)
        return obj


class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        user = request.user
        profile = get_object_or_404(Profile, user=user)
        profile_image_url = request.data.get("image_url")
        
        if profile_image_url:
            profile.profile_image = profile_image_url
            profile.save()
        
        return Response({"message": "Profile updated"})

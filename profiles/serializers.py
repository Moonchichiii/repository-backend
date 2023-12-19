from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile 


User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    profile_image = serializers.SerializerMethodField()  

    class Meta:
        model = Profile
        fields = ('username', 'bio', 'profile_image')

    def get_profile_image(self, instance):
        
        return instance.profile_image.url if instance.profile_image else None

    def display_profile(self, instance):
        
        profile_data = super().to_representation(instance)  
        profile_data['profile_image'] = self.get_profile_image(instance)
        return profile_data

from rest_framework import serializers
from .models import Post
from profiles.models import Profile



class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'user', 'image']


class PostListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'username', 'profile_image', 'created_at', 'updated_at', 'title', 'image']

    def get_username(self, obj):
        return obj.user.username
        

    def get_profile_image(self, obj):
        try:
            profile = Profile.objects.get(user=obj.user)
            return profile.profile_image.url if profile.profile_image else None
        except Profile.DoesNotExist:
                return None  

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.user


    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

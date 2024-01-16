from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile


User = get_user_model()

# user serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password')
        
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # remove confirm_password from data
        validated_data.pop('confirm_password', None)
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user)
        return user

# current user serializer
class CurrentUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='auth_token.key', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'token')
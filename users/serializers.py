from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile
from cloudinary.models import CloudinaryField



User = get_user_model()

# user Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'confirm_password')
        # set password 
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # remove confirm_password from data
        validated_data.pop('confirm_password', None)  
        user = User.objects.create_user(**validated_data)
        return user


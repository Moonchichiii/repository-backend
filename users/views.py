from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token  
from .serializers import UserRegistrationSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Create your views here.

# User registration 
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer    
    def post(self, request, *args, **kwargs):
        
        # user registration token creation

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)  
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       

# User Login View
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        
        # Authentication token retrieval
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)  
            return Response({
                'id': user.id,
                'username': user.username,
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

# User logout view

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            logout(request)
            # Logout user delete the token
            Token.objects.filter(user=request.user).delete()
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except Exception as e:
            # Log the exception
            print("Error during logout:", str(e))
            return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
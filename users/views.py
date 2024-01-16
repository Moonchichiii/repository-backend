from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from django.http import JsonResponse



# Create your views here.

# User registration 
class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            print(f"User {user.username} registered successfully")  
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        else:
            print("Registration failed. Errors:", serializer.errors)  
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
            print(f"User {user.username} logged in successfully")  
            return Response({
                'id': user.id,
                'username': user.username,
                'token': token.key
            }, status=status.HTTP_200_OK)
        else:
            print("Login failed. Invalid username or password")  
            return Response({"error": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)

# User logout view
class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            if request.user.is_authenticated:
                print(f"User {request.user.username} is authenticated")
                logout(request)
                Token.objects.filter(user=request.user).delete()
                if 'user_id' in request.session:
                    del request.session['user_id']
                return JsonResponse({"message": "Logout successful"}, status=status.HTTP_200_OK)
            else:
                print("User is not authenticated")
                return JsonResponse({"error": "Not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            print(f"Error during logout: {str(e)}")
            raise APIException(str(e))
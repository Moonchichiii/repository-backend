from django.shortcuts import render
from django.conf import settings
from cloudinary import utils
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import time
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({        
        'profiles': reverse('profiles:profile-list', request=request, format=format),
        'posts': reverse('posts:post-list', request=request, format=format),
        'comments': reverse('comments:comment-list', request=request, format=format),
        'likes': reverse('likes:like-list', request=request, format=format),
        'followers': reverse('followers:follower-list', request=request, format=format),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def generate_cloudinary_signature(request):
    timestamp = int(time.time())
    signature = utils.api_sign_request({"timestamp": timestamp}, settings.CLOUDINARY_API_SECRET)     
    return Response({
        "signature": signature,
        "timestamp": timestamp,
        "api_key": settings.CLOUDINARY_API_KEY
    })


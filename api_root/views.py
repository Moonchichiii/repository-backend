from django.shortcuts import render
from rest_framework.decorators import api_view
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

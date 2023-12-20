from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/', include('api_root.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('likes/', include('likes.urls', namespace='likes')),
    path('followers/', include('followers.urls', namespace='followers')),
    path('', lambda request: redirect('api/', permanent=False)), 
]
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls', namespace='api-users')),
 
    path('profiles/', include('profiles.urls', namespace='api-profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('likes/', include('likes.urls', namespace='likes')),
    path('followers/', include('followers.urls', namespace='followers')),

 
]

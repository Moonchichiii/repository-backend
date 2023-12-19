from django.urls import path, include
from posts import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet)


app_name = 'posts'

urlpatterns = [            
    path('', include(router.urls)),   
    
]


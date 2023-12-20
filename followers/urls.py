from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowerViewSet

router = DefaultRouter()
router.register(r'', FollowerViewSet, basename='follower')

app_name = 'followers'

urlpatterns = [
    path('', include(router.urls)),
]

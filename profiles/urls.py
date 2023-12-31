from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProfileViewSet

app_name = 'profiles'

router = DefaultRouter()
router.register(r'', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.views import ProfileViewSet


router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls')), 

    path('api/', include('api_root.urls')),

]
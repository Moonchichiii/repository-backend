from django.urls import path
from .views import api_root, generate_cloudinary_signature


urlpatterns = [
    path('', api_root, name='api-root'),
    path('cloudinary-signature/', generate_cloudinary_signature, name='generate-cloudinary-signature'),
]

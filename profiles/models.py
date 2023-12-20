from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.

User = get_user_model()
class Profile(models.Model):
    # adding user username, which is taken from user model, for a finished profile setup. 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', default='default_pfp_ivf3fa')
   
    def __str__(self):
        return f'{self.user.username} Profile'

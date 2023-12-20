from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post
from cloudinary.models import CloudinaryField
from profiles.models import Profile

# Create your tests here.


class PostViewSetTest(APITestCase):

    def setUp(self):
        # create a user
        self.user = User.objects.create_user(username='tester2023', password='2023tester')

        
        Profile.objects.create(user=self.user, bio='testing bio', profile_image='default_pfp_ivf3fa')
        

        # creating post
        self.post = Post.objects.create(user=self.user, title='posting test!!!!!!!!', content='posting content testing!!!')

    def test_posts_unauthenticated(self):        
        url = reverse('posts:post-list')
        response = self.client.get(url)

        
        self.assertNotIn('content', response.data['results'][0])

    def test_posts_authenticated(self):
        self.client.login(username='tester2023', password='2023tester')

        url = reverse('posts:post-list')
        response = self.client.get(url)
        
        #  first post in the list
        self.assertIn('content', response.data['results'][0])
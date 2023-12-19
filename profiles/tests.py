from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Profile

# Create your tests here.


class ProfileTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='tester2023', password='2023tester')



    
from django.test import TestCase
from django.urls import reverse
from .models import User

class UserModelTests(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('testpassword'))

class UserViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_registration_view(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password': 'newpassword',
        })
        self.assertEqual(response.status_code, 201)

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 200)

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile', kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)
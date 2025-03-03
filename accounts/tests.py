from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username="delowar",  email="delowar@mail.com"
        )
        self.assertEqual(user.username, "delowar")
        self.assertEqual(user.email, "delowar@mail.com")
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            username="delowar",  email="delowar@mail.com"
        )
        self.assertEqual(user.username, "delowar")
        self.assertEqual(user.email, "delowar@mail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        

class SignUpPageTests(TestCase):
    username = "testuser"
    email = "testuser@gmail.com"
    
    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there, this is signing up page")
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
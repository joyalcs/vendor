from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTest(TestCase):
    def setUp(self):
        self.user_data = {
            'username' : 'test_user',
            'email' : 'test@gmail.com',
            'password': 'testpass',
        }
        self.user = get_user_model().objects.create_user(**self.user_data)

    def test_user_register(self):
        """Test if a user is registered correctly"""
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.email, self.user_data['email'])
        self.assertTrue(self.user.check_password(self.user_data['password']))

    def test_str_user(self):
        """Test for __str__  method of user model"""
        self.assertEqual(str(self.user), self.user.username)

    def test_username_email_unique(self):
        """Test that the email and username are unique"""
        duplicate_user_data = {
            'username' : 'test_user',
            'email' : 'test@gmail.com',
            'password': 'testpass2',
        }
        with self.assertRaises(Exception) as context:
            get_user_model().objects.create_user(**duplicate_user_data)

        self.assertTrue('unique' in str(context.exception))

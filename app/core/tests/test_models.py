from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        # Test creating a user with a email successfully
        email = "mail@dev.com"
        password = "testpw123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_password_normalized(self):
        # Test that the email for a new user is normalized
        email = 'mail@DeVsItE.CoM'
        user = get_user_model().objects.create_user(email, 'testpw123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test creating a user with no email raises error
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpw123')

    def test_create_new_superuser(self):
        # Test creating a new superuser
        user = get_user_model().objects.create_superuser(
            'test@devsite.com',
            'testpw123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

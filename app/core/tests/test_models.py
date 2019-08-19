from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@testdev.com', password='testpw123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Barbeque'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Water'
        )

        self.assertEqual(str(ingredient), ingredient.name)

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "testaccounnt@example.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test that the email for a new user is normarlised"""
        email = 'test@SOMEALLCAPSDOMAIN.com'
        password = "SomePassword1234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertTrue(user.email.islower())
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'SomePassword1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        email = "testsuperuser@example.com"
        password = "supersecuresuperuser1234"
        user = get_user_model().objects.create_superuser(email=email,
                                                         password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.email.islower())
        self.assertEqual(user.email, email.lower())

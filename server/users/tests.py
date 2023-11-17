from django.contrib.auth import get_user_model
from django.test import TestCase


class UsersManagerTests(TestCase):
    def test_str_method(self):
        email = "none@test.de"
        password = "esoteric"
        user = get_user_model().objects.create(email=email, password=password)

        self.assertEqual(user.__str__(), user.email)

        user.last_name = "Michi"
        user.first_name = "King"

        self.assertEqual(user.__str__(), f"{user.last_name}, {user.first_name}")

    def test_create_user(self):
        """Test creating a user with an email is successful."""
        email = "none@test.de"
        password = "esoteric"

        user = get_user_model().objects.create(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        """Test creating a superuser."""
        email = "none@test.de"
        password = "esoteric"

        user = get_user_model().objects.create_superuser(
            email,
            password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "ceremony")

    def test_new_superuser_with_invalid_value_raises_error(self):
        """Test that creating a user without proper values raises a ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                "admin", "ceremony", is_staff=False
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(
                "admin", "ceremony", is_superuser=False
            )

from django.test import TestCase

from .models import ContactRequest


class ContactRequestsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = ContactRequest.objects.create(
            email="higher@amr.com", name="user", content="doubt"
        )

    def test_str_method(self):
        self.assertEqual(self.request.__str__(), self.request.name)

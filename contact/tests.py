from django.test import TestCase
from django.urls import reverse

from .models import ContactRequest


class ContactRequestsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = ContactRequest.objects.create(
            email="higher@amr.com", name="user", content="doubt"
        )

    def test_str_method(self):
        self.assertEqual(self.request.__str__(), self.request.name)

    def test_contact_form(self):
        response = self.client.get(reverse("contact:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact us")
        self.assertTemplateUsed(response, "contact/contact.html")

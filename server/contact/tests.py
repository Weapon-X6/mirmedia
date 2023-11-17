from django.test import TestCase
from django.urls import reverse

from .models import ContactRequest
from .forms import ContactRequestForm

from .signals import contact_request_saved
from django.db.models.signals import post_save


class ContactRequestsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # avoid sending emails during test
        post_save.disconnect(
            contact_request_saved,
            sender=ContactRequest,
            dispatch_uid="contact_request_saved",
        )
        cls.c_request = ContactRequest.objects.create(
            email="higher@amr.com", name="user", content="doubt"
        )

    def tearDown(self):
        post_save.connect(contact_request_saved, sender=ContactRequest)
        return super().tearDown()

    def test_str_method(self):
        self.assertEqual(self.c_request.__str__(), self.c_request.name)

    def test_contact_formview(self):
        response = self.client.get(reverse("contact:contact"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contact us")
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_contact_form(self):
        valid_data = {"email": "someemail@mf.com", "name": "fosfo", "content": "msg"}

        form = ContactRequestForm(valid_data)

        self.assertTrue(form.is_valid())

        form.save_request()

        requests = ContactRequest.objects.all()

        self.assertEqual(len(requests), 2)

        invalid_data = {"email": "someemailmf.com", "name": "fosfo", "content": "msg"}

        form = ContactRequestForm(invalid_data)

        self.assertFalse(form.is_valid())

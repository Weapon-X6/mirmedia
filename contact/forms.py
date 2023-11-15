from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = "__all__"

    def send_email(self):
        # todo: send-email
        ContactRequest.objects.create(
            email=self.cleaned_data["email"],
            name=self.cleaned_data["name"],
            content=self.cleaned_data["content"],
        )

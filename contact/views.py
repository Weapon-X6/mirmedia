from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ContactRequestForm


class ContactRequestFormView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactRequestForm
    success_url = reverse_lazy("blog:home")

    def form_valid(self, form):
        form.save_request()
        return super().form_valid(form)

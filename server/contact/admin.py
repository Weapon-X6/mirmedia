from django.contrib import admin

from .models import ContactRequest


class ContactRequestAdmin(admin.ModelAdmin):
    """Custom admin that only allows to read and delete objects."""

    def __init__(self, *args, **kwargs):
        super(ContactRequestAdmin, self).__init__(*args, **kwargs)
        self.readonly_fields = [f.name for f in self.model._meta.get_fields()]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    list_display = (
        "name",
        "date",
    )
    search_fields = (
        "email",
        "name",
    )
    ordering = ("date",)


admin.site.register(ContactRequest, ContactRequestAdmin)

from django.db import models


class ContactRequest(models.Model):
    email = models.EmailField()
    name = models.TextField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name

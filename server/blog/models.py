from django.conf import settings
from django.db import models


class BlogArticle(models.Model):
    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.title

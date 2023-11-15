from django.contrib import admin

from .models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "published_at")


admin.site.register(BlogArticle, BlogArticleAdmin)

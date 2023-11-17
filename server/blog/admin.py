from django.contrib import admin

from .models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("slug", "published_at")
    search_fields = (
        "title",
        "author__last_name",
        "author__first_name",
    )
    list_filter = ["author__last_name"]


admin.site.register(BlogArticle, BlogArticleAdmin)

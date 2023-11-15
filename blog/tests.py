from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import BlogArticle


def create_user(email="test@ositos.com", password="testpass", **kwargs):
    """Create and return user."""
    return get_user_model().objects.create_user(
        email=email, password=password, **kwargs
    )


class BlogArticleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = create_user(first_name="Panquecha", last_name="Bebo")
        cls.article = BlogArticle.objects.create(
            title="First Article",
            content="A very long content hopefully",
            slug="eins-slug",
            author=cls.user,
            is_online=True,
        )
        cls.article2 = BlogArticle.objects.create(
            title="Draft Article",
            content="M.I.A",
            slug="draft-article",
            author=cls.user,
        )

    def test_blog_listview(self):
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "First Article")
        self.assertContains(response, "1 of 1")
        self.assertEqual(len(response.context["blogarticle_list"]), 1)
        self.assertTemplateUsed(response, "blog/home.html")

    def test_blog_detailview(self):
        response = self.client.get(
            reverse(
                "blog:detail", kwargs={"slug": self.article.slug, "pk": self.article.id}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hopefully")
        self.assertTemplateUsed(response, "blog/detail.html")

    def test_blog_detailview_404(self):
        response = self.client.get(
            reverse("blog:detail", kwargs={"slug": self.article.slug, "pk": 2})
        )

        self.assertEqual(response.status_code, 404)

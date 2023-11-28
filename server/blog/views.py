from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import BlogArticle


class BlogArticleListView(ListView):
    template_name = "blog/home.html"
    paginate_by = 5

    def get_queryset(self):
        return BlogArticle.objects.filter(is_online=True).order_by("-published_at")


class BlogArticleDetailView(DetailView):
    model = BlogArticle
    template_name = "blog/detail.html"

    def get_object(self):
        return BlogArticle.objects.filter(
            is_online=True,
            slug=self.kwargs["slug"],
            id=self.kwargs["pk"],
        )

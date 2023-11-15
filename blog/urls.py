from django.urls import path

from .views import BlogArticleDetailView, BlogArticleListView

app_name = "blog"

urlpatterns = [
    path("", BlogArticleListView.as_view(), name="home"),
    path(
        "article/<slug:slug>-<int:pk>", BlogArticleDetailView.as_view(), name="detail"
    ),
]

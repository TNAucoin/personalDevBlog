from django.urls import path, re_path
from .views import PostListView, PostDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    re_path(
        r"^(?P<pk>[a-zA-Z0-9]+)/(?P<slug>[-\w\d]+)/$",
        PostDetailView.as_view(),
        name="post",
    ),
    re_path(r"^(?P<pk>[a-zA-Z0-9]+)/$", PostDetailView.as_view(), name="post_id"),
]

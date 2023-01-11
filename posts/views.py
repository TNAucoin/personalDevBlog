from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "post_list_view.html"
    context_object_name = "post_list"
    queryset = Post.objects.filter(is_published=True)


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail_view.html"
    context_object_name = "post"
    queryset = Post.objects.filter()

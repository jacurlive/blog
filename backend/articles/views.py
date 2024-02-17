from typing import Any
from django.views.generic import ListView, DetailView
from .models import About, ImagePost, Blog



class MainView(ListView):
    model = About
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['images'] = ImagePost.objects.all()

        return context
    

class AboutView(ListView):
    queryset = About.objects.first()
    template_name = "blog/aboutme.html"
    context_object_name = "about"


class BlogView(ListView):
    model = About
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        context["articles"] = Blog.objects.order_by("-created_at")

        return context
    

class BlogDetailView(DetailView):
    template_name = "blog/blog_details.html"
    query_pk_and_slug = "slug"
    queryset = Blog.objects.all()
    context_object_name = "blog"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.first()
        return context

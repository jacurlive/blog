from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import About, ImagePost



class MainView(ListView):
    # queryset = About.objects.first()
    template_name = "blog/index.html"
    context_object_name = "about"

    def get_queryset(self):
        about = About.objects.first()
        print(about)
        # image_post = ImagePost.objects.all()
        context = {
            "about": about,
            # "image": image_post
        }
        print(context)
        return context

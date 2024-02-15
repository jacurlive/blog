from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import About, Blog, ImagePost


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    fields = ("full_name", "specialization", "image", "instagram_link", "github_link", "linkedin_link", "telegram_link", "short_bio", "bio")


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):
    fields = ("title", "content")


@admin.register(ImagePost)
class ImagePostAdmin(SummernoteModelAdmin):
    fields = ("image", "content")

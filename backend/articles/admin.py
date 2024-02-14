from django.contrib import admin

from .models import About, Blog, ImagePost


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = ("full_name", "specialization", "image", "instagram_link", "github_link", "linkedin_link", "telegram_link", "short_bio", "bio")


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ("title", "content")


@admin.register(ImagePost)
class ImagePostAdmin(admin.ModelAdmin):
    fields = ("image", "content")

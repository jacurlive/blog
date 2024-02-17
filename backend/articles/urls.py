from django.urls import path

from .views import MainView, BlogView, BlogDetailView, AboutView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<str:slug>/", BlogDetailView.as_view(), name="post"),
    path("about/", AboutView.as_view(), name="about")
]

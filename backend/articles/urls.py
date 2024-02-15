from django.urls import path

from .views import MainView, BlogView, BlogDetailView

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("blog/", BlogView.as_view(), name="blog"),
    path("blog/<str:slug>/", BlogDetailView.as_view(), name="post")
]

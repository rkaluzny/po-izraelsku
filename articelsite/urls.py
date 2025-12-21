from django.urls import path

from . import views
from .views import ArticleDetailView

urlpatterns = [
    path("blog/<slug:slug>/", ArticleDetailView.as_view(), name="artikel_detail"),
    path("blog/", views.blogOverview, name="blog_overview"),
    path("themes/israel/", views.blogOvervieIsrael, name="blog_overview_israel"),
    path("themes/testimonies/", views.blogOvervieTestimonies, name="blog_overview_testimonies"),
    path("themes/bible/", views.blogOvervieBible, name="blog_overview_bible"),
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("about-us/", views.aboutUs, name="about_us"),
    path("email-send/", views.contact, name="send_email"),
]
import datetime
import os

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from hitcount.models import HitCountMixin, HitCount

def background_image_path(instance, filename):
    ext = filename.split('.')[-1]
    new_name = f"background-img-{instance.slug}.{ext}"
    return os.path.join("images/blog-imgs", new_name)

# Create your models here.
class Articel(models.Model, HitCountMixin):
    THEMES = [
        ("israel", "Israel"),
        ("bible", "Bible"),
        ("testimonies", "Testimonies"),
    ]


    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=False, max_length=200)
    theme = models.CharField(
        max_length=20,
        choices=THEMES,
        default="israel",
    )
    background_img = models.ImageField(upload_to=background_image_path, blank=False)
    author = models.CharField(max_length=200, blank=False)
    text = models.TextField(max_length=100000)
    pub_date = models.DateTimeField("date published", blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return 'Title: ' + self.title + ' | Writen by: ' + self.author + ' | Last edit: ' + str(self.pub_date)
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
import datetime

from django.db import models
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify


def generate_id():
    return get_random_string(6)


class Post(models.Model):
    id = models.CharField(
        primary_key=True, unique=True, max_length=6, default=generate_id
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=False, max_length=100)
    date = models.DateField(max_length=25)
    publish_date = models.DateField(default=datetime.date.today())
    is_published = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=500)
    content = models.TextField()
    rendered_content = models.TextField()

    class Meta:
        ordering = ["-publishDate"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug, "pk": self.id})

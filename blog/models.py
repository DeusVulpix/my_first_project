from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    some = models.BooleanField()

    def get_absolute_url(self):
        return reverse("article:article-detail", kwargs={"id": self.id})

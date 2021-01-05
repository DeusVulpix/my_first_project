from django.db import models
from django.urls import reverse

class Products(models.Model):
    title       = models.CharField(max_length=40)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(decimal_places=3, max_digits=300)
    show        = models.BooleanField(default=False)
    summary     = models.TextField(blank=False,null=False)

    def absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"

from django.db import models
from django.shortcuts import reverse


class ProductCategory(models.Model):
    name = models.CharField()
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    categories = models.ManyToManyField(ProductCategory)
    name = models.CharField()
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.IntegerField(default=0) # Prices are in cents

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-detail', kwargs={'slug': self.slug})

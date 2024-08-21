from django.db import models
from django.shortcuts import reverse


class ProductCategory(models.Model):
    name = models.CharField()
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/products/?category={self.slug}'


class Product(models.Model):
    categories = models.ManyToManyField(ProductCategory)
    name = models.CharField()
    slug = models.SlugField()
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product-detail', kwargs={'slug': self.slug})

    def get_image_path(self):
        return f'shop/images/products/{self.slug}.jpg'

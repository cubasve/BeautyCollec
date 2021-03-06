from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CATEGORIES = (('S', 'Skincare'), ('M', 'Makeup'), ('A', 'Accessory'))


class Product(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('products_detail', kwargs={'pk': self.id})


class Brand(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    founded = models.IntegerField()
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'brand_id': self.id})


class Purchase(models.Model):
    date = models.DateField('purchase date')
    category = models.CharField(max_length=1,
                                choices=CATEGORIES,
                                default=CATEGORIES[0][0])

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_category_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

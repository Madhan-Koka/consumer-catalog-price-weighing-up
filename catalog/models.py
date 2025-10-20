from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    site = models.CharField(max_length=50)
    image_url = models.URLField(blank=True, null=True)

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    checked_at = models.DateTimeField(auto_now_add=True)

class PriceAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    target_price = models.FloatField()
    notified = models.BooleanField(default=False)


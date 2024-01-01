from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=200, default="Uncategorized")
    subcategory = models.CharField(max_length=200, default="Uncategorized")
    brandName = models.CharField(max_length=200)
    displayName = models.CharField(max_length=500)
    heroImage = models.CharField(max_length=300)
    moreColors = models.IntegerField()
    displayPrice = models.DecimalField(max_digits=7, decimal_places=2)
    displayRating = models.DecimalField(max_digits=4, decimal_places=3)





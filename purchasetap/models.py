from django.db import models
from django.contrib.auth.models import User

# class Users

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchase_name')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{} by {} on {}'.format(self.product.name, self.seller.username, self.created.strftime("%A, %d. %B %Y %I:%M%p"))

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'

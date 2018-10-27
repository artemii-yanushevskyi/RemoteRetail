from django.db import models
from django.contrib.auth import get_user_model

# User = get_user_model()


class Patron(models.Model):
    nickname = models.CharField(max_length=40)
    email = models.CharField(max_length=20, null=True)
    

class Wallet(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    patron = models.OneToOneField(
        Patron, related_name='wallet', on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = ' Wallets'


class Good(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Good'
        verbose_name_plural = 'Goods'


class Purchase(models.Model):
    # good = models.ForeignKey(
    #     Good, on_delete=models.CASCADE,
    #     related_name='purchases', related_query_name='purchase'
    # )
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    seller = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='buyer')
    created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Purchase'
        verbose_name_plural = 'Purchases'



from django.db import models
from django.utils import timezone

class Patron(models.Model):
    nickname = models.CharField(max_length=40)
    email = models.CharField(max_length=20, null=True)
    balance = models.IntegerField(default=0)


class Purchase(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name='buyer')



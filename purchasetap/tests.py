from django.test import TestCase
from purchasetap.models import Purchase, Product
from django.contrib.auth.models import User


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="lion", price=3.3)
        Product.objects.create(name="vata", price=34.43)

    def test_products(self):
        lion = Product.objects.get(name="lion")
        vata = Product.objects.get(name="vata")
        self.assertEqual(float(lion.price), 3.3)
        self.assertEqual(float(vata.price), 34.43)


class PurchaseTest(TestCase):
    def setUp(self):
        u = User.objects.create(username='denis')
        p = Product.objects.create(name='vata')
        Purchase.objects.create(seller=u, product=p)
        print('asdfasdf')

    def test_purchase(self):
        u = User.objects.get(username='denis')
        purchase = Purchase.objects.get(seller=u)
        self.assertEqual(purchase.product.name, 'vata')

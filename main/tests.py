from django.test import TestCase
from main.models import Product

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            name='nasi uduk',
            amount=100,
            description='adalah makanan enak'
        )

    def test_product(self):
        self.assertEqual(self.product1.slug, 'nasi-uduk')
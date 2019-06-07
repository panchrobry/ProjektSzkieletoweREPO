from django.test import TestCase
from .models import *
# Create your tests here.
class CategoryCreationTest(TestCase):
    def setUp(self):
        Category.objects.create(Description = "bla bla")
    def test_category(self):
        category = Category.objects.get(Description = "bla bla")
        self.assertEqual(category.Description,'bla bla')

# Hitting external endpoint
import requests

def get_products():
  endpoint = 'https://example.com/api/products'
  response = requests.get(endpoint)
  results = response.json()
  return results

# Filter 4 stars or higher

products = [{"product": "Shoes", "price": 35, "rating": 4.2},
{"product": "White Hat", "price": 21, "rating": 4.8},
{"product": "Blue Hat", "price": 21, "rating": 3.8},
{"product": "Brown Shirt", "price": 27, "rating": 4.0}]

def get_four_or_more(products):
    return [rated for rated in products if rated["rating"] >= 4]

# Test example
import unittest
# from ... import get_four_or_more

class TestProductFilter(unittest.TestCase):
    def test_length(self):
        results = get_four_or_more(products)

        self.assertEqual(len(results), 3)

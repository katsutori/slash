import requests

def get_products():
  endpoint = 'https://example.com/api/products'
  response = requests.get(endpoint)
  results = response.json()
  return results

products = [{"product": "Shoes", "price": 35, "rating": 4.2},
{"product": "White Hat", "price": 21, "rating": 4.8},
{"product": "Blue Hat", "price": 21, "rating": 3.8},
{"product": "Brown Shirt", "price": 27, "rating": 4.0}]

def get_four_or_more(products):
    return [rated for rated in products if rated["rating"] >= 4]

print(get_four_or_more(products))

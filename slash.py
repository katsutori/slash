import requests

def get_products():
  endpoint = 'https://example.com/api/products'
  response = requests.get(endpoint)
  results = response.json()
  return results

products = [{"product": "Shoes", "price": 35, "rating": 4.2},
{"product": "White Hat", "price": 21, "rating": 4.8},
{"product": "Blue Hat", "price": 21, "rating": 3.8}]


# target = [rated for rated in products if rated["rating"] >=4]
# print(target)

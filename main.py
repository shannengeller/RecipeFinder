from distutils.version import Version
from setuptools import setup, find_packages

#example
import spoonacular as sp
api = sp.API("0d267ca4d1e149f58e3164a5ce2dbd59")

# Parse an ingredient
response = api.parse_ingredients("3.5 cups King Arthur flour", servings=1)
data = response.json()
print(data[0]['name'])


# Detect text for mentions of food
response = api.detect_food_in_text("I really want a cheeseburger.")
data = response.json()
print(data['annotations'][0])


# Get a random food joke
response = api.get_a_random_food_joke()
data = response.json()
print(data['text'])



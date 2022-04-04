from distutils.version import Version
from setuptools import setup, find_packages
from apiKey import key

#example
import spoonacular as sp
api = sp.API(key)

# Print beginning stuff
print("Welcome to the Recipe Finder!")
print()
print("If you would like to see a full recipe, please enter 'full'")
print("If you would like to see a list of ingredients, please enter 'list'")
print("If you would like to see a list of recipes, please enter 'recipes'")
print("If you would like to see a list of ingredients, please enter 'ingredients'")
print()

# Get user input
user_input = input("Please enter 'full', 'list', 'recipes', or 'ingredients': ")

# If user input is 'full'
if user_input == "full":
    print("Please enter the name of the recipe you would like to see: ")
    recipe_name = input()
    print("Searching for recipe... with " + recipe_name)
    
# if user is 'list'
elif user_input == "list":
    print("Please enter the name of the ingredient you would like to see: ")
    ingredient_name = input()
    print("Searching for ingredients... with " + ingredient_name)

# if user is 'recipes'
elif user_input == "recipes":
    print("Please enter the name of the ingredient you would like to see: ")
    ingredient_name = input()
    print("Searching for recipes... with " + ingredient_name)

# if user is 'ingredients'
elif user_input == "ingredients":
    print("Please enter the name of the recipe you would like to see: ")
    recipe_name = input()
    print("Searching for ingredients... with " + recipe_name)


# Print error message
else:
    print("Not a valid input. Please try again.")


#random example code (not used) - just showing how to use the API from their website/ReadMe

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



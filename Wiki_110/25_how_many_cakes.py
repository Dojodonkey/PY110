'''
# Pete is baking cakes and needs help calculating
# how many he can make with his recipes and available ingredients.
# Write a function cakes() that takes two dictionaries:
#  the recipe and the available ingredients.
# Return the maximum number of cakes Pete can bake.

# Rules:
# - Ingredients not present in the objects can be considered as 0.

P:
- input: 2 arguments.
    - the recipe, available ingredients (both dictionaries)
- output: integer (amount of cakes made)

- explicits:
    - using the recipe, compare it to the ingredients available and return how many cakes can be made.
    - missing ingredients are equivalent to 0.
- implicits:
    - available ingredients may be 0.

- questions:
    - are you hungry yet?

D:
- tuples from dictionaries.
- a copy of the recipe as not to modify the original
- integer to deal with quantities related

A:
- High level strategy -
first create a copy of the available ingredients to not modify the original.
I intend to modify it, subracting values from it using
values from the recipe. Then iterating over the copy of the avail ingredients,
first if any of the keys from the recipe are not in the avail ingredients, return 0.
Then, i need to find the lowest value in the available ingredients.
Init 'cakes' to 0.
Then while the value of that ingredient is greater than zero, deduct the value from the
ingredient in recipe. At every iteration, add 1 to 'cake'
return 'cake'.

1. init 'cake_count' to 0.
2. check if all keys in 'recipe' are in 'ingredients'.
    - if not, return 0.
3. find the lowest value in 'ingredients'.
4. while the value of that lowest key is greater than 0,
deduct the value of the ingredient in 'ingredients' by the value in 'recipe'
    - for each iteration, add 1 to 'cake_count'.
5. return 'cake_count'.

C:
'''

def cakes(recipe, pantry):
    # check if ingredients are missing or pantry is empty
    if not all(ingredient in pantry.keys() for ingredient in recipe.keys()) or not pantry:
        return 0
    # create a dictionary containig only ingredients needed
    pantry_copy = {ingredient: amount for ingredient, amount in pantry.items() if ingredient in recipe}
    cake_count = []
    # make cakes using ingredients
    for ingredient, amount in pantry_copy.items():
        count = 0
        while amount >= recipe[ingredient]:
            amount -= recipe[ingredient]
            count +=1
        cake_count.append(count)
    # take the fewest amount of cakes made
    return min(cake_count)



# must return 2
print(cakes({"flour": 500, "sugar": 200, "eggs": 1},
      {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}) == 2)

# # must return 11
print(cakes({"cream": 200, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
      {"sugar": 1700, "flour": 20000, "milk": 20000, "oil": 30000, "cream": 5000}) == 11)

# # must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
      {"sugar": 500, "flour": 2000, "milk": 2000}) == 0)

# # must return 0
print(cakes({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
      {"sugar": 500, "flour": 2000, "milk": 2000, "apples": 15, "oil": 20}) == 0)

# # must return 0
print(cakes({"eggs": 4, "flour": 400}, {}) == 0)

# # must return 1
print(cakes({"cream": 1, "flour": 3, "sugar": 1, "milk": 1, "oil": 1, "eggs": 1},
      {"sugar": 1, "eggs": 1, "flour": 3, "cream": 1, "oil": 1, "milk": 1}) == 1)

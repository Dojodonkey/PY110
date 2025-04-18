'''
problem statment:
One of the most frequently used real-world string operations is that of "string substitution,"
where we take a hard-coded string and modify it with various parameters from our program.

Given the object shown below, print the name, age, and gender of each family member:
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Each output line should follow this pattern:
# (name) is a (age)-year-old (male or female).

# expected output:
# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.

for member in munsters:
    name = member
    age = munsters[member]['age']
    gender = munsters[member]['gender']
    print(f'{name} is a {age}-year-old {gender}.')
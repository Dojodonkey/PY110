'''
Problem Statement:
Given a dictionary where both keys and values are unique,
invert this dictionary so that its keys become values and its values become keys.

- High level strategy:
    - return a dictionary with all original values as keys mapped to original keys as values.
'''
def invert_dict(dictionary):
    return {value: key for key, value in dictionary.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }))
print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
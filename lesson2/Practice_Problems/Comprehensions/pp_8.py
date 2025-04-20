'''
problem statement:
Given the following data structure,
write some code to return a list that contains the colors of the fruits and the sizes of the vegetables.
The sizes should be uppercase, and the colors should be capitalized.
'''
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def modify(sub_dict):
    if sub_dict['type'] == 'fruit':
        return [color.capitalize() for color in sub_dict['colors']]
    elif sub_dict['type'] == 'vegetable':
        return sub_dict['size'].upper()

result = [modify(value) for value in dict1.values()]

print(result)

# expected result:
# [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
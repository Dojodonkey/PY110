'''
Problem Statement:
Given a dictionary and a list of keys,
produce a new dictionary that only contains the key/value pairs for the specified keys.
'''
def keep_keys(dct, lst):
    return {key: value for key, value in dct.items() if key in lst}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

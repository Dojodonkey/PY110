'''
problem statement:
This problem may prove challenging.
Try it, but don't stress about it.
If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure,
write some code to return a list that contains
only the dictionaries where all the numbers are even.
'''

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def is_evens(dict_element):
    for value_lst in dict_element.values():
        if not all([value % 2 == 0 for value in value_lst]):
            return False
    return True

even_dict_list = [element_dict for element_dict in lst if is_evens(element_dict)]

print(even_dict_list)

# expected result:
# [{e: [8], f: [6, 10]}]
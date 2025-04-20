'''
problem statement:
Given the following data structure,
write some code that defines a dictionary where the key is the first item in each sublist,
and the value is the second.
'''

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
lst_dict = {list[0]: list[1] for list in lst}
print(lst_dict)

# expected result:
# # Pretty printed for clarity
# {
#     'a': 1,
#     'b': 'two',
#     'sea': {'c': 3},
#     'D': ['a', 'b', 'c']
# }
'''
problem statement:
Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order as strings
(that is, the numbers should be treated as strings).
Use a comprehension if you can. (Try using a for loop first.)
'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
sorted_lst = [sorted(nest_lst, key=str) for nest_lst in lst]
print(sorted_lst)

# expected results:
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]
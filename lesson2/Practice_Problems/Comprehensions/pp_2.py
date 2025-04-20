'''
Problem Statement:
Given the following data structure, return a new list with the same structure,
but with the values in each sublist ordered in ascending order.
Use a comprehension if you can. (Try using a for loop first.)
'''
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
sorted_list = [sorted(list) for list in lst]
print(sorted_list)

# expected result:
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]
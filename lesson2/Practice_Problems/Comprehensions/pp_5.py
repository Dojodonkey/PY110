'''
problem statement:
Given the following data structure,
sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain.
You shouldn't mutate the original list.
'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def total_odds(a_list):
    return sum([element for element in a_list if element % 2 != 0])

sorted_subs = sorted(lst, key=total_odds)
print(sorted_subs)
# expected result:
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
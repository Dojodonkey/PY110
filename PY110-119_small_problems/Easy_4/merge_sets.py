'''
Problem Statment:
Given two lists, convert them to sets and return a new set which is the union of both sets.
'''
def merge_sets(lst1, lst2):
    return set(set(lst1) | set(lst2))

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True
'''
Problem Statement:
Write a function that takes two list arguments,
each containing a list of numbers,
and returns a new list that contains the product of each pair of numbers
from the arguments that have the same index.
You may assume that the arguments contain the same number of elements.
'''
def multiply_list(lst1, lst2):
    # using list comprehension:
    return [lst1[i] * lst2[i] for i in range(len(lst1))]

    # using conventional for loop
    # result = []
    # for i in range(len(lst1)):
    #     result.append(lst1[i] * lst2[i])
    # return result
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
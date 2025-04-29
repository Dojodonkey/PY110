'''
You want to multiply all elements of a list by 2.
However, the function is not returning the expected result.
Explain the bug, and provide a solution.
'''

# def multiply_list(lst):
#     for item in lst:
#         item *= 2

#     return lst

# print(multiply_list([1, 2, 3]) == [2, 4, 6])
# integers are immutable. So when we use augmented reassignment,
# the item is reassigned to a new value but the element, being a number,
# remains unchanged. A solution would be to use element reassignment or a list comprehension.
# element reassignment:
def multiply_list(lst):
    for i in range(len(lst)):
        lst[i] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
# list comprehension:
def multiply_list(lst):
    return [num * 2 for num in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])
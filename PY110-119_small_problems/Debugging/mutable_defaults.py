'''
We want to create a function that appends a given value to a list. However, the function seems to be behaving unexpectedly:
'''

# def append_to_list(value, lst=[]):
#     lst.append(value)
#     return lst

# print(append_to_list(1) == [1])
# print(append_to_list(2) == [2])
# How would you fix this code?
# The problem lies in the behaviour of the mutable default argument.
# # 'lst' is a list, a mutable object and stores elements across multiple function calls.
# By assigning the default parameter to None,
# the function can use a conditional to check if the argument is truthy
# and if not, creates an empty list to append 'value' to.

def append_to_list(value, lst=None):
    if not lst:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
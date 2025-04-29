'''
We defined a function intending to multiply the sum of numbers by a factor.
However, the function raises an error. Why? How would you fix this code?
'''
def sum_by_factor(numbers, factor): # changed function name
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_by_factor(numbers, 2)==20)
# this code raises a TypeError as 'sum' within the function is used as a built-in function,
# while the name of the function 'sum' is attempted to be used within it. Because 'sum' accepts
# 2 arguments in the function definition, when it is used within the local namespace with only 1 argument,
# a TypeError is thrown.
# To fix this bug, we could simply re-name the function being defined.
'''
Create a function that takes a list of integers as an argument.
The function should determine the minimum integer value that can be
appended to the list so the sum of all the elements
equals the closest prime number that is greater than the current sum of the numbers.
For example, the numbers in [1, 2, 3] sum to 6.
The nearest prime number greater than 6 is 7.
Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

P:
- input: list
- output: integer

- explicits:
    - return the difference between the sum of the input list and the next prime number.
- implicits:
    none.

- questions: none

D:
- integer as the sum of the list.
- integer as the next prime number after the sum.
- integer, the value of the difference between the two.
- range to use a sequence up to the sum.


A:
- HL -
find the sum of the list. then find the next prime number after that sum.
return the value of the difference between the two.

1. init 'sum_' to the sum of the input list.
2. init 'value_' to 'sum_'.
3. check if 'value_' is a prime number.
    - if it is, add 1 to it's value.
4. iterate through a range, starting at 2 and stopping at 'value_'.
    - if any num in that range is a multiple, add 1 to 'value_'.
5. return the value of 'value_' - 'sum_'

C:
'''

def nearest_prime_sum(lst):
    sum_ = sum(lst)
    value_ = sum_

    if all(value_ % num != 0 for num in range(2, value_)):
        value_ += 1

    while any(value_ % num == 0 for num in range(2, value_)):
        value_ += 1

    return value_ - sum_


print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)
'''
# Given a List [] of n integers, find the minimum number to be inserted
# in the list, so that the sum of all elements of the list should
# equal the closest prime number.

P:
- input: list of integers
- output: integer

- explicits:
    - the sum of all elements need to equal a prime number.
    - add a number to the list so that, that happens.
    - (the nearest prime number to the sum of the original list)
- implicits:
    - prime number is only divisible by 1 and itself.
    - if the sum of input is a prime number, return 0.

- questions: none

D:
- integer to store the sum of the input list.
- range to divide potential numbers by.
A:
- High Level -
first find the sum of the input list. Then find the next prime number after that value.
then subtract the prime number by the sum of the list. return that number.

1. init 'sum_' to sum of the input list.
2. find the nearest prime number.
    - use a 'counter' that starts at 'sum_'.
        - if 'counter' is only divisible by itself and 1,
        return 'sum_' - 'counter'.
        - add 1 to 'counter' if 'counter' is not prime.

C:
'''
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def minimum_number(lst):
    sum_ = sum(lst)
    tracker = sum_

    while not is_prime(tracker):
        tracker += 1

    return tracker - sum_


print(minimum_number([3,1,2]) == 1)
print(minimum_number([5,2]) == 0)
print(minimum_number([1,1,1]) == 0)
print(minimum_number([2,12,8,4,6]) == 5)
print(minimum_number([50,39,49,6,17,28]) == 2)
'''
A prime number is a positive number that is evenly divisible only by itself and 1.
Thus, 23 is prime since its only divisors are 1 and 23.
However, 24 is not prime since it has divisors of 1, 2, 3, 4, 6, 8, 12, and 24.
Note that the number 1 is not prime.

Write a function that takes a positive integer as an argument
and returns true if the number is prime, false if it is not prime.

You may not use any of Python's add-on packages to solve this problem.
Your task is to programmatically determine whether a number is
prime without relying on functions that already do that for you.

P:

- input: integer
- output: boolean value

- explicit rules:
    - if a number is prime, meaning its only divisors are itself and 1, return True, otherwise False.
    - 1 is not a prime number (edge case)
- implicit rules:
    - none

- questions: none

E:
```python
print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
```
D:

- ranges to check if numbers are divisible by input

- High Level Strategy:
    - iterate over a sequence of numbers up, the stopping point being the input integer
    and if any of those numbers result in no remainder when by divided by the input integer,
    return False.

A:
1. iterate over a sequence of numbers beginning at 2 and stopping at the input integer (exclusive).
2. if any of those numbers result in no remainder, return False. Otherwise return True.

C:
'''
def is_prime(number):
    if number == 1:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True
'''
Create a function that takes a single integer argument
and returns the sum of all the multiples of 7 or 11 that are less than the argument.
If a number is a multiple of both 7 and 11, count it just once.

For example,
the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22.
The sum of these multiples is 75.

If the argument is negative, return 0.

P:
- input: integer
- ouput: integer

- explicits:
    - find all the multiples of 7 or 11 that are less than the input integer.
    - if an integer is a multiple of both 7 and 11, count it only once.
    - return the sum of all those multiples.
    - if the input integer is 0 or less than 0, return 0.
- implicits:
    - none

- questions: none

D:
- set to contain multiples of 7 or 11.
    - avoids reoccurrences of integers that are multiples of both 7 and 11.
- integer that is sum of set. (to be returned)
- range to select integers that are multiples.

A:
- HL -
iterate through a sequence of numbers, stopping point is the input integer.
if that number is a multiple of 7 or 11, add it to a set.
return the sum of that set.

1. init 'multiples' to an empty set.
2. iterate through a range, starting at 1, and stopping at input integer.
    - if the integer is a multiple of 7 or 11, append it to 'multiples'.
3. return the sume of 'multiples'.

C:
'''
def is_mult(integer):
    return integer % 7 == 0 or integer % 11 == 0

def seven_eleven(num_):
    if num_ < 1:
        return 0

    multiples = []

    for number in range(1, num_):
        if is_mult(number):
            multiples.append(number)

    return sum(multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)
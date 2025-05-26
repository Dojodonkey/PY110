'''
Write a function, persistence, that takes in a positive parameter
`num` and returns its multiplicative persistence, which is the number
of times you must multiply the digits in `num` until you reach a single digit.

P:
input: integer
output: integer

- explicits:
    - return multiplacative persistance of input number.
        - number of times the digits of input number need to be multiplied to each other,
        until you reach a single digit.
- implicits:
    - none

- questions:
    - none

D:
- list to split up the input number and use a function to multiply elements to each other.
- integer, a count, keeping rounds when the list is multiplied.

A:
- High Level -
Create a list containing the digits of the input value. until the len of the list is 1, multiply the elements
of the list together. Upon each iteration, add 1 to a 'count'.

1. import math module
2. init helper fuction to split a converted string of num into a list,
containing digits making up 'num'.
3. init 'num_split' to a list containing digits from input.
4. use a while loop to multiplying elements to each other until the product is a single digit (len 1).
    at every iteration, reassign 'num_split' to the product of 'num_split'
5. keep 'count' adding 1 at every iteration of multiplication.
'''
import math

def split_num(num):
    return [int(digit) for digit in str(num)]

def persistence(num):
    num_split = split_num(num)
    count = 0

    while len(num_split) > 1:
        product = math.prod(num_split)
        num_split = split_num(product)
        count += 1

    return count



print(persistence(39)) # should return 3, because 3*9=27, 2*7=14, 1*4=4
# and 4 has only one digit
print(persistence(999)) # should return 4, because 9*9*9=729, 7*2*9=126,
# 1*2*6=12, and finally 1*2=2
print(persistence(4)) # should return 0, because 4 is already a one-digit number
print(persistence(25)) # should return 2, because 2*5=10, and 1*0=0
'''
Create a function that takes a string argument
that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string.
The argument will always have more than 4 digits.

P:
- input: string of digit chars
- output: integer

- explicits:
    - return the greatest product of four consecutive digits in the string.
    - the input string will always have atleast 4 digit chars.
- implicits:
    - none

- questions: none

D:
- integer to keep the max product of sub-digits.
- string to create substrings.
    - integers of converted substrings.
- list of digits making up input string.
- dictionary with substrings (4 consec digits) mapped to the product of digits.

A:
- HL -
find the product of all cosecutive digits (4). return the greatest one.

1. init 'max_prod' to 0.
2. iterate through input string.
    - use slicing.
        - convert to digits and find the product.
            - import math and use product module.
    - if the product is greater than 'max_product',
    reassign 'max_product' to that value.
3. return 'max_prod'

C:
'''
import math

def greatest_product(strng):
    # using a slice to find the greatest product.
    max_prod = 0

    for i in range(len(strng)):
        prod_ = math.prod([int(digit) for digit in strng[i : i + 4]])
        if prod_ > max_prod:
            max_prod = prod_

    return max_prod

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6
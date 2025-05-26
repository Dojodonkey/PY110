'''
# Complete the greatestProduct method so that it'll find the greatest product of five consecutive digits
# in the given string of digits.

P:
- input: string of numbers
- output: integer (largest possible product)

explicits:
    - find the largest product possible from 5 consecutive digits in input string.
implicits:
    - none

questions:
    - none

D:
- integer to store greatest product. (eventually returned)
- list contains substrings of input string, always 5 at a time.
- range to iterate through input string.

A:
- High Level Strategy -
iterate over input string. create a an empty list. iterate over the input string again, stopping at the 6 char
after i (if i is less than i - len of list). if not just use the rest of the list.
add those chars to the list. find the product of that list and if it's greater than any previous list,
that product is the current greatest.

1. init 'greatest_prod' to 0.
2. iterate through input list.
    - init 'prod_list' to an empty list.
    3. iterate through a substring of the input list,
    starting at the currect char and stopping 5 chars after.
    (if the index of the current char + 4 is less than len of input list. if not true, iterate through
    the rest of the list.)
        - add those chars to 'prod_list'
    4. find the product of digits in 'prod_list'
        - if it is greater than 'greatest_prod', reassign 'greatest_prod'
5. return 'greatest_prod'
'''
import math

def get_prod(lst):
    return math.prod(int(char) for char in lst)

def greatest_product(strng):
    greatest_prod = 0
    for i in range(len(strng)):
        prod_list = []
        if i + 4 < len(strng):
            for j in range(i, i+5):
                prod_list.append(strng[j])
        else:
            prod_list.extend(list(strng[i:]))
            break

        if get_prod(prod_list) > greatest_prod:
            greatest_prod = get_prod(prod_list)

    return greatest_prod



print(greatest_product("123834539327238239583") == 3240)
print(greatest_product("395831238345393272382") == 3240)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("92494737828244222221111111532909999") == 5292)
print(greatest_product("02494037820244202221011110532909999") == 0)
'''
# Given an integer n, find the maximal number you can obtain by deleting
# exactly one digit of the given number.

P:
- input: integer
- output: integer

- explicits:
    - find the greatest number possible to obtain by deleting 1 digit from the input integer.

D:
- list to iterate over the digits in the number.
- string to iterate over the digit chars in the number.
- integer to keep a record of the greatest number found so far.

A:
- High Level Strategy -
init 'max_value' to 0.
Break down the input integer into a list to iterate through the digits.
Remove a digit, find the value of remaining digits put together
and if it is greater than 'max_value', reassign 'max_value' to that digit.
Do this process for every digit it in input integer.

1. init 'max_value' to 0.
2. create a list of digits made up from the input integer.
3. iterate over that list.
    - remove the digit from the list.
    - put the digits back together
    - if that integer is greater than 'max_value',
    reassign 'max_value' to that integer.
'''
def make_num(lst):
    return int(''.join(lst))

def delete_digit(input_int):
    max_value = 0
    int_split = [num for num in str(input_int)]

    for i in range(len(int_split)):
        int_split_copy = int_split.copy()
        int_split_copy.remove(int_split_copy[i])
        if make_num(int_split_copy) > max_value:
            max_value = make_num(int_split_copy)

    return max_value

print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)
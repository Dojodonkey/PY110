'''
Write a function that rotates the last count digits of a number.
To perform the rotation,
move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

P:

- input: integer and count(integer)
- output: rotated integer

- explicit rules:
    - take a number, counting from the last digit 'count' times, remove that digit and place it as the last digit.
- implicit rules:
    - integers are immutable
    - integers are not sequences

- questions: none

E:

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

D:

- strings to create an indexed sequence.
- list to remove and place elements easily.

High Level Strategy:
    - find the digit counting backwards by -1 'count' times, remove it and place it as the last digit.

A:
1. convert the integer into a string and create a list of all digit chars.
2. find the digit char counting from the back of the list 'count' times, remove it, and place it as the last digit char in the list.
3. join all the chars in list
4. convert it to an integer and return it.

C:
'''
def rotate_rightmost_digits(integer, count):
    digits = list(str(integer))
    return int(''.join(digits + [digits.pop(-count)]))


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

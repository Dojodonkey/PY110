'''
Take the number 735291 and rotate it by one digit to the left, getting 352917.
Next, keep the first digit fixed in place and rotate the remaining digits to get 329175.
Keep the first two digits fixed in place and rotate again to get 321759.
Keep the first three digits fixed in place and rotate again to get 321597.
Finally, keep the first four digits fixed in place and rotate the final two digits to get 321579.
The resulting number is called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns the maximum rotation of that integer.
You can (and probably should) use the rotate_rightmost_digits function from the previous exercise.

P:

- input: integer
- output: integer (maximum rotation of input)

- explicit rules:
    - beginning from the first element until the the second to last integer is rotated,
    place elements to the back of the integer.
- implicit rules:
    - integers are immutable.
    - the second digit will be the first digit in the final integer.

- questions: none

E:

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

D:

- strings for a index sequence
- list to easily move elements

A:
1. convert the integer to a string
2. create a list to easily move elements.
3. iterate through the list beginning at the first element.
    - place the element at the back of the list.
    - the next iteration, moves the element of the next index.
4. join the elements back into a string.
5. convert the string back into an integer

C.
'''
def max_rotation(number):
    digits = list(str(number))
    for i in range(len(digits)):
        digits = digits + [digits.pop(i)]
    return int(''.join(digits))


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True
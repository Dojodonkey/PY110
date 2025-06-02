'''
Create a function that takes a string of digits as an argument
and returns the number of even-numbered substrings that can be formed.
For example, in the case of '1432',
the even-numbered substrings are '14', '1432', '4', '432', '32', and '2',
for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

P:
- input: string of digit chars
- output: integer

- explicits:
    - return the amount of even numbered substrings that can be made from input string.
    - if a substring occurs more than once, include both occurrences in amount returned.
- implicits:
    - input string contains only digit chars.

- questions: none

D:
- list to contain all possible even numbered substrings.
- integers to check if they are even.
- integer to be returned (the len of the list)

A:
- HL -
iterate a converted integer of the input string.
beginning with the first integer, check if it is even, if so, add it to a list.
then create new digits with the next integer and check it again. add it to the list if it is even.
return the length of that list.

1. convert the input string into a list of integers.
2. init 'evens' to an empty list.
3. iterate over that list of integers.
    - 'num_' is the first integer.
        - if it is even, append it to evens.
    - iterate through the rest of the integers (sliding window) and build up 'num'.
        - check if 'num_' is even at each iteration and if so append it to 'evens'.
4. return the length of 'evens'.

C:
'''
def is_str_even(strng):
    return int(strng) % 2 == 0

def even_substrings(strng):
    strng_digits = list(strng)
    evens = []

    for i in range(len(strng_digits)):
        num_ = strng_digits[i]
        if is_str_even(num_):
            evens.append(num_)
        for j in range(i + 1, len(strng_digits)):
            num_ += strng_digits[j]
            if is_str_even(num_):
                evens.append(num_)

    return len(evens)

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

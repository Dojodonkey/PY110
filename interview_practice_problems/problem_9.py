'''
Create a function that takes two string arguments
and returns the number of times that the second string occurs in the first string.
Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

P:
- input: string and potential substring
- output: integer

- explicits:
    - return the number of occurrences of substring in string.
    - overlapping strings don't count.
        - when a substring occurrs, the next substring cannot contain any chars at the index of the previous substring.
- implicits:
    - none

- questions: none

D:
- integer to store the count of occurrences of substring. (to be returned)
- dictionary with substring as key and occurrences as values.

A:
- find the amount of occurrences of the substring in the string and return that value.
'''
def count_substrings(strng, substr):
    return strng.count(substr)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)
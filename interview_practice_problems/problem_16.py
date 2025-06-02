'''
Create a function that returns the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string.
You may assume that the input string contains only alphanumeric characters.

P:
- input: string
- output: integer

- explicits:
    - return the count of distinct characters of input string that occur more than once.
    - case-insensitive
    - all chars are alphanumeric
- implicits: none

- questions: none

D:
- list that contains all chars that occur more than once in input string.
- integer, the length of that list. (to be returned)

A:
- HL -
create a list of all chars that occur more than once in the input string.
return the length of that list.

1. convert the input string to lower case.
2. init 'repeatables' to an empty list.
3. iterate through input string.
    - if a char occurs more than once, append it to 'repeatables'.
4. return the length of 'repeatables'.
'''
def distinct_multiples(strng):
    repeatables = set([char for char in strng.lower()
                       if strng.lower().count(char) > 1])

    return len(repeatables)



print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5
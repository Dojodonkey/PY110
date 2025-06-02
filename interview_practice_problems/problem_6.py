'''
Create a function that takes a string argument
and returns a dict object in which the keys represent the lowercase letters in the string,
and the values represent how often the corresponding letter occurs in the string.

P:
- input: string
- output: dictionary

- explicits:
    - return a dictionary with chars as keys mapped to occurrences of those chars
    in input string as values.
    - only lower case chars need to be mapped.
- implicit:
    - only alphabetical chars should be mapped.

- questions: none

D:
- dictionary to be returned.
- integer to contain count of char.
- boolean to check if char is lower case and alphabetical.

A:
- HL -
iterate through the input string. select char only if it is lower case and alphabetical.
add the char as a key and count of char as a value if the char is not in the dictionary.
return that dictionary.

C:
'''
def count_letters(strng):
    return {char: strng.count(char)
            for char in strng
            if char.islower() and char.isalpha()}


expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
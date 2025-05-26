'''
Write a function that takes a string as an argument and groups the
number of times each character appears in the string as a dictionary
sorted by the highest number of occurrences.

The characters should be sorted alphabetically, and you should ignore
spaces, special characters, and count uppercase letters as lowercase ones.

P:
- input: strng
- output: dictionary

- explicits:
    - return a dictionary with counts as keys and a list,
    sorted alphabetically, of chars with that count.
- implicits:
    - no empty lists in the dict. Meaning non-existent counts are left out.
    - space chars are not counted.

- questions: none

D:
- dictionary for the output
    - count of char as key
    - list of chars as value

A:
- High Level-
first iterate a dictionary. Then iterate through alphanumerical chars in the string.
if they return a count greater than 0 and that count is not in the dictionary,
add it and a list containing char as a value. If it is already in the dict,
append the char to the list value.
then iterate through the completed dictionary and sort the list values alphabetically.
finally sort the dictionary keys in descending order.

1. init 'count_dict' to an empty dict.
2. iterate over the input string.
    - if the char is alphanumeric, find the count.
        - if the count is not in the dictionary, add it as a key with a list and char as an element.
        - if it is just append the char to the list value.
3. iterate over 'count_dict'.
    - sort the list values alphabetically.
4. return a dict with keys in descending order.
'''
def get_char_count(strng):
    count_dict = {}
    strng = strng.lower()

    frequency = {}
    for char in strng:
        if char.isalnum():
            frequency.setdefault(strng.count(char), []).append(char)

    for key, value in frequency.items():
        frequency[key] = sorted(set(value))

    return dict(sorted(frequency.items(), reverse=True))



print(get_char_count("Mississippi")) # should return {4: ['i', 's'], 2: ['p'], 1: ['m']}
print(get_char_count("Hello. Hello? HELLO!!")) # should return {6: ['l'], 3: ['e', 'h', 'o']}
print(get_char_count("aaa...bb...c!")) # should return {3: ['a'], 2: ['b'], 1: ['c']}
print(get_char_count("aaabbbccc")) # should return {3: ['a', 'b', 'c']}
print(get_char_count("abc123")) # should return {1: ['1', '2', '3', 'a', 'b', 'c']}

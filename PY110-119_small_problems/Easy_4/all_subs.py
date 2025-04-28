'''
All Substrings:

P:
- input: string
- output: list sorted

- rules:
    - function returns a list of substrings from a string.
    - order the list based on the order of occurrence of each char.

Strategy:
- return a sorted list by iterating through the string, beginning  with the first character
and after the entire string has been iterated, do it again beginning at the second char,
and so on.

Algorithm:
1. split the string into a list of characters
2. create an empty list to move built substrings into.
3. build substrings and remove the first character after.
    - clear the first element of the listed string after every complete iteration.
4. repeat iterations until there are no characters left to begin iteration of strng.
'''
def substrings(strng):
    char_lst = list(strng)
    sub_lst = []
    sub_str = ''

    while char_lst:
        for char in char_lst:
            sub_str += char
            sub_lst.append(sub_str)
        char_lst.pop(0)
        print(sub_str)
        sub_str = ''
    return sub_lst

print(substrings('abcde'))


expected_output = [
    'a', 'ab', 'abc', 'abcd', 'abcde',
    'b', 'bc', 'bcd', 'bcde',
    'c', 'cd', 'cde',
    'd', 'de',
    'e',
]
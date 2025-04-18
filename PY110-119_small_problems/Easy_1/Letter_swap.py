'''
Problem Statement:
Given a string of words separated by spaces,
write a function that swaps the first and last letters of every word.
You may assume that every word contains at least one letter,
and that the string will always contain at least one word.
You may also assume that each string contains nothing but words and spaces,
and that there are no leading, trailing, or repeated spaces.

Understanding the Problem:
- input: string
- output: string

- explicit rules:
    - the first and last letters need to be swapped in every word in the input string.
    - all strings contain at least 1 word.
    - there will be no leading, trailing or repeated spaces.
- implicit rules:
    - none

- questions:
    - none

Examples/Test Cases:

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

- Observations:
    - strings contain only alphabetic characters

Data Structures:
- Lists to contain words from the input string


Algorithm:
    1. define 'swap' to accept 1 parameter 'strng'.
    2. initialize 'split_str' to a list containing all words in 'strng'.
    3. initialize 'swapped_list' to an empty list.
    4. iterate through 'split_str':
        1. initialize 'list_word' to a list containing all characters of each word.
        2. make a copy of 'list_word'.
            - needed for element reassignment
        3. initialize 'first_char' to the first element in 'list_word_copy'.
        4. initialize 'last_char' to the last element in 'list_word_copy'.
        5. reassign the first and last elements in 'list_word' to 'last_char' and 'first_char'.
        6. append 'list_word' converted explicitly into a string to 'swapped_list'.
    5. return 'swapped_list' as a string.

Code:
'''
def swap(strng):
    split_str = strng.split()
    swapped_list = []

    for word in split_str:
        list_word = list(word)
        list_word_copy = list_word.copy()
        first_char = list_word_copy[0]
        last_char = list_word_copy[-1]

        list_word[0] = last_char
        list_word[-1] = first_char
        swapped_list.append(''.join(list_word))

    return ' '.join(swapped_list)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
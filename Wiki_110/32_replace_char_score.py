'''
# Given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

P:
- input: string
- output: string

- explicits:
    - replace every letter in a string with its position in the alphabet.
    - if char is not alphabetic, ignore and don't include in output string.
- implicits:
    - char values are seperated by a space.
    - no seperator per say to identify words in ouput string.

- questions: none

E:
p alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
p alphabet_position("-.-'") == ""

D:
- string to modify original and ouput.
- integer to store positional value of char.
- string to contain new ouput string (not modifying original).
- list to contain values of chars of words of input string.

A:
- High Level Strategy -
init 'result' to an empty list. Then iterate through a list of words from input string.
Iterate through word and append the value of each char,
converted into a string, to result. Then join 'result' using a space as seperator as return value.

1. init 'result' to an empty list.
2. init 'strng_split' into a list of words from input string.
3. iterate through 'strng_split'.
    - if the char is not alphabetic, ignore it.
    - find the value of the char converted to lower case,
    and append that value converted as a string to 'result'.
4. return a joined 'result' with a space between each member element.

C:
'''
def get_value(char):
    return str(ord(char.lower()) - 96)

def alphabet_position(strng):
    # strng_split = strng.split()
    # result = []

    # for word in strng_split:
    #     for char in word:
    #         if char.isalpha():
    #             result.append(get_value(char))

    # return ' '.join(result)

    # using list comprehension and ternary expression
    return ' '.join([get_value(char) for word in strng.split()
                     for char in word if char.isalpha()])

print(alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
print(alphabet_position("-.-'") == "")
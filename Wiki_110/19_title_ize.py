'''
A string is considered to be in title case if each word in the string is either:
a) Capitalized (that is, only the first letter of the word is in upper case)
b) Considered to be an exception and put entirely into lower case unless it is the first word,
which is always capitalized.

Write a function that will convert a string into title case,
given an optional list of exceptions (minor words).
The list of minor words will be given as a string with each word separated by a space.
Your function should ignore the case of the minor words string --
it should behave in the same way even if the case of the minor word string is changed.

P:
- input: 2 arguments
    - the str to be converted to title case, a string of exceptions.
- ouput: str converted

- explicits:
    - convert the first string into title case.
    - the second string contains words that are exceptions and should be returned in lower case.
    - the first word in the output string should always be in title case.
- implicits:
    - sometimes only 1 argument is given.
    - strngs and exceptions vary in case.

D:
- list to convert string word by word.

A:
- High Level -
init the function 'title_case' and use a default parameter for 'exceptions' to an empty strng.
Then init 'result' to an empty list.
Make sure to check words comparing lower case words to each other.
Split the input string into a list containing lower case words, and iterate through it.
If the word is not in the exceptions list, converted to lower case, capitalize it.
If it is and it is not the first word, it should be lower case.
Append the word to result.
Join the words in result and return it.

C:
'''

def title_case(strng, exceptions=''):
    strng_split = strng.lower().split()
    exceptions = exceptions.lower()
    result = []

    # using a if/else block
    for word in strng_split:
        if word not in exceptions or word == strng_split[0]:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return ' '.join(result)

    # using a one liner, list comprehension
    return ' '.join([word.capitalize() if word not in exceptions.lower()
                     or word == strng.lower().split()[0]
                     else word.lower() for word in strng.lower().split()])

print(title_case('a clash of KINGS', 'a an the of')) # should return 'A Clash of Kings'
print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return 'The Wind in the Willows'
print(title_case('the quick brown fox')) # should return 'The Quick Brown Fox'

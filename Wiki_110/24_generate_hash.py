'''
Write a function `generate_hashtag(s)` that generates a hashtag from the given string `s`.

Rules:
- The hashtag must start with a '#' symbol.
- All words in the hashtag must start with a capital letter.
- If the resulting hashtag is longer than 140 characters, the function should return `False`.
- If the input string or the resulting hashtag is an empty string, the function should return `False`.

P:
- input: string
- ouput: string (hastag)

- explicits:
    - return a hashtag from the input string.
        - starts with '#' and first char is capitalized.
    - if length is greater than 140 chars or string is empty, return False.
- implicits:
    - none

- questions:
    - why are we doing this? #fuckX

D:
- list to split the string and then join it.
- string method to modify the input string.

A:
- High Level Strategy -
return a concatenated string to '#' after replacing spaces with no space and using titlecase.

1. convert the string to titlecase.
2. replace all spaces with non-spaces.
3. if the string is empty return False.
4. concatenate to '#' and return.

C:
'''
def generate_hashtag(strng):
    hash = '#' + strng.title().replace(' ', '')

    if 1 < len(hash) <= 140:
        return hash

    return False

print(generate_hashtag(""))                       # should return False
print(generate_hashtag(" " * 200))                # should return False
print(generate_hashtag("Do We have A Hashtag"))   # should return "#DoWeHaveAHashtag"
print(generate_hashtag("Nice To Meet You"))       # should return "#NiceToMeetYou"
print(generate_hashtag("this is a test"))         # should return "#ThisIsATest"
print(generate_hashtag("code " * 35))             # should return False (result would be 141 chars)
print(generate_hashtag("a" * 139))                # should return "#" + "A" + "a" * 138
print(generate_hashtag("a" * 140))                # should return False (result would be 141 chars)

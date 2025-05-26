'''
# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols and return the final state of the string.

P:
- input: string
- ouput: cleaned up string

- explicits:
    - treat chars with '#' as backspace chars.
    - return a cleaned up string.

D:
- string to return new cleaned up string.

p clean_string('abc#d##c') == "ac"
p clean_string('abc####d##c#') == ""

A:
- High Level -
split the string up into chars. iterate over that list.
if a char is '#' remove it and the char before it. Do this until all '#' are gone.
return a joined list.

1. split input string into a list of chars.
2. iterate through that string while '#' exists in it.
3. iterate character by character.
    - if the char is '#', remove it and the char preceding it.
4. return a joined list of remaining chars.
'''

def clean_strings(strng):
    strng_lst = list(strng)

    while '#' in strng_lst:
        for char in strng_lst:
            if char == '#':
                strng_lst.remove(strng_lst[strng_lst.index(char) - 1])
                strng_lst.remove(char)

    return ''.join(strng_lst)

print(clean_strings('abc#d##c') == "ac")
print(clean_strings('abc####d##c#') == "")
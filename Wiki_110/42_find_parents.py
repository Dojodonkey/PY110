'''
# Mothers arranged a dance party for the children in school. At that party,
# there are only mothers and their children. All are having great fun on the
# dance floor when suddenly all the lights went out. It's a dark night and no
# one can see each other. But you were flying nearby and you can see in the
# dark and have ability to teleport people anywhere you want.
# Legend:
# - Uppercase letters stands for mothers, lowercase stand for their children,
# i.e. "A" mother's children are "aaaa".
# - Function input: String contains only letters, uppercase letters are unique.

P:
- input: string
- output: strng

- explicits:
    - rearrange the strings so that all uppercase chars are before their equivalent
    lower case chars.
- implicits:
    - the return string is sorted alphabetically.
    - there is always an equivalent lower case char to an upper case char.
    - empty string, returns an empty string.

- questions: none

D:
- string to create substrings containing first the upper case char,
followed by the lower case char/s.
- dictionary containg upper case chars as keys
and lower case chars as values.
- a list to sort the created substring,
based on the first char of the substring
(the upper case char)

A:
- high level strategy -
create an empty dictionary, 'parent_and_kids'.
then iterate through the input string.
if the char is upercase place is as a key
and the value will be the count of the lower case char multiplied by the char.
then create a list made of concatenated strings from the keys and values of 'parent_and_kids'.
Then sort this list based on the first char of each string.
return a joined string of all elements of the list.

1. init 'parent_kids' to an empty dict.
2. iterate through the input string.
    - if the char is uppercase,
    make it a key and map it to the value of the lower case equivalent times the count of the lower case equivalent.
3. init 'pk_strings' to a list of concatenated string of key, value pairs in 'parent_kids'.
4. sort 'pk_strings' based on the first char of each element.
5. return a joined string of elements in 'pk_strings'

C:
'''
def find_children(strng):
    pk_dict = {}

    for char in strng:
        if char.isupper():
            pk_dict[char] = char.lower() * strng.count(char.lower())

    pk_list = [key+value for key, value in pk_dict.items()]
    pk_list.sort()

    return ''.join(pk_list)

print(find_children("abBA") == "AaBb")
print(find_children("AaaaaZazzz") == "AaaaaaZzzz")
print(find_children("CbcBcbaA") == "AaBbbCcc")
print(find_children("xXfuUuuF") == "FfUuuuXx")
print(find_children("") == "")
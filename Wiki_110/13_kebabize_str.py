'''
Modify the kebabize function so that it converts a camel case string into a
kebab case. Kebab case separates words with dashes '-'; camel case identifies
separate words by upcasing the first character in each new word.

P:
- input: string (camelCase)
- output: string (kebab-case)

- explicits:
    - kebab case seperates words w/ dashes.
    - camel case seperates words w/ upper case chars.
- implicits:
    - camel case starts w/ a lower case char.
    - if the input string contains a non-alpha char, it is removed.

- questions: none

E:
kebabize('camelsHaveThreeHumps') # should return 'camels-have-three-humps'
kebabize('myCamelHas3Humps') # should return 'my-camel-has-humps'

D:
- string to contain kebab case output.

A:
High level-
first create an empty string.
Then iterate through the input string. add chars if lower case.
if not, add '-' to string and then the char lowercased.
if char is non-alpha, do nothing.

1. init 'kebab' to an empty string.
2. iterate over input string.
    - if char is alpha and lowercased, add to 'kebab'
    - if char is uppercased, add '-' and then char lowercased to 'kebab'
3. return 'kebab'

C:
'''
def kebabize(strng):
    '''
    creates a new string with converted camel case to kebab
    '''
    kebab = ''

    for char in strng:
        if char.islower() and char.isalpha():
            kebab += char
        elif char.isupper() and char.isalpha():
            kebab += '-' + char.lower()


    return kebab

print(kebabize('camelsHaveThreeHumps')) # should return 'camels-have-three-humps'
print(kebabize('myCamelHas3Humps')) # should return 'my-camel-has-humps'

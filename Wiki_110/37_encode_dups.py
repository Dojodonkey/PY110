'''
# The goal of this exercise
# is to convert a string
#  to a new string where
# each character in the new string
# is "(" if that character appears only once
# in the original string, or ")" if that character appears
# more than once in the original string.
# Ignore capitalization when determining if a character is a duplicate.

P:
- input: string
- output: string

- explicits:
    - return a string based on the input string.
    - each char is '(' is that character appears only once, or ')'
    is that char appears more than once.
    - comparisons are case-insensitive.
- implicits:
    - spaces count as chars.

D:
- list to contain chars as they appear.
- integer to contain count of char.
- dictionary to keep count.
- string for output.

A:
- High Level Strat -
init 'code' to an empty string. iterate through the input string.
check the count of each char lowercased.
if the count is greater than 1, add ')' and if not,
then add '(' to 'code'. return 'code'

1. init 'code' to an empty string.
2. iterate through input string.
    - if the count of that char, lowercased, is greater than 1,
    concatenate ')', if not, '('.
3. return 'code'

C:
'''
def duplicate_encode(strng):
    code = ''
    strng = strng.lower()

    # for char in strng:
    #     count_ = strng.count(char)
    #     if count_ > 1:
    #         code += ')'
    #     else:
    #         code += '('

    # return code

    # using list comprehension with a ternary expression
    return ''.join([')' if strng.count(char) > 1
                    else '(' for char in strng])

print(duplicate_encode("din") == "(((")
print(duplicate_encode("recede") == "()()()")
print(duplicate_encode("Success") == ")())())")
print(duplicate_encode("(( @") == "))((")

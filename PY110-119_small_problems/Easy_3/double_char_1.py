'''
Problem Statement:
Write a function that takes a string, doubles every character in the string, then returns the result as a new string.
'''
def repeater(strng):
    return ''.join([char * 2 for char in strng])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

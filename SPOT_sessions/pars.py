#   Create a function that takes a string containing only parentheses (( and )) and determines if the parentheses are balanced. A balanced string has the same number of opening and closing parentheses, and each closing parenthesis has a corresponding opening parenthesis that comes before it.
'''
P:
- input: string
- output: bool

- explicits:
    - return a bool regarding a balance of '()'.
    - each closing par needs an opening par to be balanced.
    - for True, we need to same amount of opening pars as closing,
    and each closing par needs an opening par before it.
- implicits:
    - if input string empty, return True.

D:
- list containing pars.
    - while finding pairs, remove them the list.
    - if any pars are left over would false.
- integer to count pairs.
- string to compare opening and closing pars.
- set to find occurrences of both opening and closing.
    - if these values are different False.
- range to iterate through pars.
- list to contain integers of pars already paired.

A:
-HL-
iterate through the string.
if a par is closing, check if any previous pars are opening.
if they there are and the index is not in 'used_pars', add the indexes of closing and opening par to  'used_pars'.
after iterating through the intire string. if the len of strng and len of 'used_pars' is equal return True.
if not return False.

1. init 'used_pars' to an empty list.
2. iterate through input list.
    - if par is closing, check if there are opening pars in the previous chars
    whose indexes are not in 'used_pars'.
        - if so, find the index of opening par.
            - add the index of closing and opening par to 'used_list'.
        - if not, return False.
3. by default, return True

C:
'''
def is_balanced(pars):
    if not pars:
        return True

    used_pars = []

    for i in range(len(pars)):
        if pars[i] == ')':
            for j in range(len(pars[:i])):
                if (pars[j] == '('
                    and j not in used_pars
                    and i not in used_pars):
                    used_pars.extend([i, j])

    return len(used_pars) == len(pars)

print(is_balanced("()") == True)
print(is_balanced(")(") == False)
print(is_balanced("(())") == True)
print(is_balanced("())") == False)
print(is_balanced("((())())") == True)
print(is_balanced("((())()))") == False)
print(is_balanced("()()()()") == True)
print(is_balanced("") == True)
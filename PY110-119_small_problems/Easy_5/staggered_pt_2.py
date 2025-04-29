'''
Problem:
Modify the function from the previous exercise so it ignores
non-alphabetic characters when determining whether it should uppercase or lowercase each letter.
The non-alphabetic characters should still be included in the return value;
they just don't count when toggling the desired case.
'''
def staggered_case(strng):
    stag = ''
    switch = True
    for char in strng:
        if switch == True and char.isalpha():
            stag += char.upper()
            switch = False
        elif not char.isalpha():
            stag+= char
        else:
            stag+= char.lower()
            switch = True
    return stag

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
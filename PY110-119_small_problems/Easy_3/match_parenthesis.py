'''
Problem Statement:
Write a function that takes a string as an argument
and returns True if all parentheses in the string are properly balanced, False otherwise.
To be properly balanced, parentheses must occur in matching '(' and ')' pairs.
'''
def is_balanced(strng):
    par = 0
    for char in strng:
        if char == '(':
            par +=1
        elif char == ')':
            par -= 1
        if par < 0:
            return False
    return par == 0


print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
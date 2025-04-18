'''
problem statement:
Given the following code, what will the final values of a and b be? Try to answer without running the code.
'''
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2    # reassigns element but does not reassign the variable a to a new integer value.
lst[1][0] -= a # 5 - 2 = 3

print(a) # 2
print(b) # [3, 8]
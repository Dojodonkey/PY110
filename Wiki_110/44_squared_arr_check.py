'''
# Given two arrays a and b write a function comp(a, b) that checks whether
# the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in `b` are the elements in `a` squared,
# regardless of the order.
'''
def comp(a, b):
    if not a or not b or len(a) != len(b):
        return False
    a.sort()
    b.sort()
    for i, j in zip(a, b):
        if j // i != i:
            return False
    return True


print(comp([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361]) == True)
print(comp([121, 144, 19, 161, 19, 144, 19, 11], [132, 14641, 20736, 361, 25921, 361, 20736, 361]) == False)
print(comp(None, [1, 2, 3]) == False)
print(comp([1, 2], []) == False)
print(comp([1, 2], [1, 4, 4]) == False)

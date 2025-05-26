'''
# Sort the given strings in alphabetical order, case insensitive.

P:
- input: list of words
- ouput: list of words sorted alpabetically

- explicits:
    - sort the input list alphabetically
    - sorting is not dependent on case.

D:
- list for sorted output.
    - a new list as to not modify the original.

A:
- High Level -
return a new list sorted alphabetically. Sort should not take case into account.

p sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"]
p sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"]
'''
def first_char(word):
    return word[0].lower()

def sortme(lst):
    return sorted(lst, key=first_char)


print(sortme(["Hello", "there", "I'm", "fine"]) == ["fine", "Hello", "I'm", "there"])
print(sortme(["C", "d", "a", "Ba", "be"]) == ["a", "Ba", "be", "C", "d"])
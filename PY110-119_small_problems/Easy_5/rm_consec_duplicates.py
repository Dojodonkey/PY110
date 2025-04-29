'''
Given a sequence of integers,
filter out instances where the same value occurs successively,
retaining only the initial occurrence.
Return the refined sequence.
'''
def unique_sequence(lst):
    uniques = []
    for idx, char in enumerate(lst):
        if not uniques:
            uniques.append(char)
        elif char != lst[idx - 1]:
            uniques.append(char)
    return uniques

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
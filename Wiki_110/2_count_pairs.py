
'''
Write a function that takes a list of integers as input and counts the number of
pairs in the list. A pair is defined as two equal integers separated by some
other integer(s).

P:
- input: list of integers
- output: integer (total amount of pairs)

- explicit rules:
    - count the number of pairs in a list.
    - a pair is defined as two of the same integers seperated by some other integers.
- implicit rules:
    - none

- questions: none

D:

- range to iterate through the input list.
- a list to store pairs.
- integer to keep count of the amount of pairs.

A:
- High Level Strategy:
We want to iterate through the input list, checking if the list contains more than one of each element.
If so, we want to check if the same element is next to it in the list.
If that's not the case, we update our counter by 1.


1. initialize 'count' to 0 (will store pairs)
2. compare one element at a time.
3. compare that element with all other elements after it in the list.
3. if two elements are equal to each other:
    - check if integers between them are different.
    - update a 'count' by 1.
C:
'''

def pairs(lst):
    count = 0
    length_ = len(lst)
    for i in range(length_):
        if lst.count(lst[i]) == 1:
            # if there are no duplicates, skip to next iteration
            continue
        for j in range(i + 2, length_): # avoiding neighboring pairs
            if lst[i] == lst[j]:
                k = lst[i+1: j] # list containing ints between i and j
                if all(x != lst[i] for x in k): # checks if all ints in k are not equal to int at idx i
                    count += 1
    return count

# Examples:
print(pairs([1, 2, 5, 6, 5, 2])) #--> 2
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])) # --> 4
# provided by LSbot:
print(pairs([1, 2, 1]))              # Should return 1 (1 appears twice with 2 between)
print(pairs([1, 2, 3, 1]))           # Should return 1
print(pairs([5, 5, 5]))              # Should return 0 (no integers between duplicates)
print(pairs([1, 2, 1, 3, 1]))        # Should return 2 (two pairs of 1's)
print(pairs([1, 2, 3, 4, 2, 5, 6]))  # Should return 0 (the 2's are separated but no complete pair)
# i don't understand why LSbot does not count the last test case as NOT a pair.
# but as far as i can tell the code holds up against the test cases.

print('-' * 40) #formatting line to compare outputs

# here's LSbot's solution:
def pairs(lst):
    """
    Count pairs of equal integers separated by at least one different integer.

    Args:
        lst: A list of integers

    Returns:
        The number of pairs found in the list
    """
    count = 0
    for i in range(len(lst)):
        for j in range(i + 2, len(lst)):
            # Check if values match and there's at least one different value between them
            if lst[i] == lst[j] and any(lst[i] != lst[k] for k in range(i + 1, j)):
                count += 1
    return count

# Examples:
print(pairs([1, 2, 5, 6, 5, 2])) #--> 2
print(pairs([1, 2, 2, 20, 6, 20, 2, 6, 2])) # --> 4  *incorrect*
# provided by LSbot:
print(pairs([1, 2, 1]))              # Should return 1 (1 appears twice with 2 between)
print(pairs([1, 2, 3, 1]))           # Should return 1
print(pairs([5, 5, 5]))              # Should return 0 (no integers between duplicates)
print(pairs([1, 2, 1, 3, 1]))        # Should return 2 (two pairs of 1's) *incorrect*
print(pairs([1, 2, 3, 4, 2, 5, 6]))  # Should return 0 (the 2's are separated but no complete pair)
                                        #(contradicting but output actually correct)

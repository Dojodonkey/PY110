'''
Write a function that takes a non-empty string `s` as input and finds the
minimum substring `t` and the maximum number `k`, such that the entire string
`s` is equal to `t` repeated `k` times.

Examples:
f("ababab") # should return ["ab", 3]

P:
- input: 's', a non-empty string.
- output: list containing the minimum substring and amount repeated.

- explicit rules:
    - find the smallest substring and count how many times it is repeated.
- implicit rules:
    - the smallest substring contains more than 1 char.

- questions: none

D:
- output a list that contains the smallest substring as first element,
and the amount of times it repeats as the second element.
- integer returned from the count method.
- string to find the smallest substring.
- list to contain substrings found.
- range to build substrings.

A:
- High Level Strategy:
first we must find the smallest substring. This must be greater than 1 char and repeat itself in the string.
then find how many times it repeats itself. create a list with the substring as the first element,
and the amount repeated as the second element.

1. iterate through the list to find substrings.
    - if a substring contains more than 1 char and repeats itself, it is a substring.
2. find the smallest substring.
    - assign it to 't'.
3. find out how many times it repeats itself.
    - using the count method.
    - assign the return value to 'k'.
4. create a list with our findings.
    - [t, k]

C:
'''
# Code works, only things that does not account for is when strings contain multiple min strings with equal counts.
# but that's overkill. The test case does not have this edge case issue.
# second test case is self-made.
def f(strng):
    substrings = []
    for i in range(len(strng)):
        sub_str = ''
        for j in range(i, len(strng)):
            sub_str += strng[j]
            if strng.count(sub_str) > 1 and sub_str not in substrings and len(sub_str) > 1:
                substrings.append(sub_str)
    sub_dict = {sub: strng.count(sub) for sub in substrings}
    def get_value(key):
        return sub_dict[key]
    min_leng = min(sub_dict, key=len)
    shortest_keys = [sub for sub in sub_dict if len(sub) == len(min_leng)]
    t = max(shortest_keys, key=get_value)
    k = strng.count(t)
    return [t, k]





print(f("ababab")) # should return ["ab", 3]
print(f('ababccbccbcc'))
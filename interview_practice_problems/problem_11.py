'''
Create a function that takes a nonempty string as an argument
and returns a tuple consisting of a string and an integer.
If we call the string argument s,
the string component of the returned tuple t,
and the integer component of the tuple k, then s, t, and k
must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring
and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

P:
- input: string
- output: tuple

- explicits:
    - return a tuple containing a substring of the input string and an integer.
    - the input string is made up of potential the same substring multiple times.
        - figure out what substring makes up the input string.
        - figure out how many times that substring is repeated.
        - return these two figures in a touple.
- implicits:
    - if the input string does not have any repetitive substrings,
    return a tuple with the input string and the integer 1.
    - the substring used needs to be the longest substring that is repetitively occurring.

- questions: none

D:
- string to build up substrings.
- a list to store the substrings.
- integer to find the longest substring.
- integer to find the occurrences of that substring.

A:
- HL -
iterate through the input string.
build substrings found and append them to a list.
find the longest substring. It must occur more than once.

1. init 'subs_' to an empty list.
2. create a sliding window using nested for loops and build substrings.
    - append substrings to 'subs_'.
3. if the longest substring in 'subs' multiplied by it's occurrences is not equal to input string,
remove it from the list.
    - if it does, return a tuple with that substring and occurrences in a tuple.
4. repeat step 3 until 'subs_' is empty.
    - if 'subs_' is empty, return a tuple with the input string and 1.
'''
def count_(sub_str, strng):
    return strng.count(sub_str)

def repeated_substring(strng):
    subs_ = []

    for i in range(len(strng)):
        sub_str = ''
        for j in range(i, len(strng)):
            sub_str += strng[j]
            if (count_(sub_str, strng) > 1
                and count_(sub_str, strng) * sub_str == strng
                and sub_str not in subs_):
                subs_.append(sub_str)

    if not subs_:
        return (strng, 1)

    max_sub = max(subs_, key=strng.count)
    max_sub_count = count_(max_sub, strng)

    return (max_sub, max_sub_count)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))
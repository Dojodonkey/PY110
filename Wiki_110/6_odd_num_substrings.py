'''
Write a function that takes a string of integers as input and returns the
number of substrings that result in an odd number when converted to an integer.

P:
- explicit rules:
    - make as many odd substrings converted to integers as possible.
    - check if they are odd and keep track of how many odd numbers can be made.
- implicit rules:
    - none

- questions: none


E:
solve("1341") # should return 7
1 - odd
13 - odd
134 - even
1341 - odd
3 - odd
34 - even
341 - odd
4 - even
41 - odd
1 - odd
total - 7

solve("1357") # should return 10
1 - odd
13 - odd
135 - odd
1357 - odd
3 - odd
35 - odd
357 - odd
5 - odd
57 - odd
7 - odd
total - 10

D:
- integer to create 'sub numbers' out of substrings.
- integer to keep track of total odd 'sub_numbers'
- list to contain 'sub_numbers'
- integer to return length of that list

A:
High-Level-Strategy:
initialize a variable beginning with the first char in the substring converted to an integer.
we then check if it is an odd number. if it is, let's append it to a list.
add the next char again converted to that variable. Check again and repeat until all chars are added and checked.
Then iterate through starting at the next char and repeat.

1. initialize 'sub_str' to an empty string.
2. initialize 'odd_subs' to an empty list.
3. iterate through the input string.
    1. concatenate the char to 'substring'
    2. convert 'substring' to an integer and check if it is odd.
    3. if it is, append it to 'odd_subs'.
        - if not, just add the next char to 'substring' and repeat.
4. return the length of 'odd_subs'.

C:
'''
def solve(strng):
    odd_subs = []
    sub_str = ''
    while strng:
        for num in strng:
            sub_str += num
            if int(sub_str) % 2 != 0:
                odd_subs.append(int(sub_str))
        strng = strng[1:] if len(strng) > 1 else None

    return len(odd_subs)

print(solve("1341")) # should return 7
print(solve("1357")) # should return 10

# Solution using nested iteration:
def solve(strng):
    count = 0
    #making substrings beginning at each char in str
    for i in range(len(strng)):
        sub = ''
        #adding substring to sub starting from i
        for j in range(i, len(strng)):
            sub += strng[j]
            #checking if the integer value is odd
            if int(sub) % 2 != 0:
                count += 1

    return count


print(solve("1341")) # should return 7
print(solve("1357")) # should return 10
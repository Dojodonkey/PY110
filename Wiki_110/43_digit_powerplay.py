'''
# Some numbers have funny properties. For example:
# 89 --> 8¹ + 9² = 89 * 1
# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
# 46288 --> 4³ + 6⁴ + 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
# Given a positive integer n written as abcd... (a, b, c, d... being digits)
# and a positive integer p we want to find a positive integer k, if it exists,
# such as the sum of the digits of n taken to the successive powers of p is
# equal to k * n.
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
# = n * k
# If it is the case we will return k, if not return -1.
# Note: n and p will always be given as strictly positive integers.

P:
- input: two integers
    - n (number containg digits to work with)
    - p (starting point for successive powers)
- ouput: integer
    - k

- explicits:
    - return the result of all the digits of 'n' factored by 'p' successively, added together.
        - if its equal to n * k, return k, else -1

D:
- list to split up the digits.

A:
- High Level:
iterate through 'n' digit by digit using 'p' to successively factor each digit. Append the result to a new list
and find the sum of it. Then divide that sum by 'n'. If it is a whole number, return it, if not return -1.

1. create a list, 'n_lst', of digits that make up 'n'.
    - convert is to a string, make a list of those chars converted back to digits.
2. Then init 'factored_lst' to an empty list.
3. iterate through 'n_list' and factor each digit successively using 'p' as the starting digit.
    - append the output of that factor expression to 'factored_lst'.
4. find the sum of 'factored_lst'
5. divide 'n' by that sum.
    - if there is no remainder, return the result.
    - if so, return -1

p dig_pow(89, 1) == 1
p dig_pow(92, 1) == -1
p dig_pow(46288, 3) == 51
p dig_pow(695, 2) == 2
'''
def dig_pow(n, p):
    n_lst = [int(char) for char in str(n)]
    factored_lst = []
    factor = p

    for digit in n_lst:
        factored_lst.append(digit ** factor)
        factor += 1


    if list(str(sum(factored_lst) / n))[-1] == '0':
        return sum(factored_lst) // n
    else:
        return -1



print(dig_pow(89, 1) == 1)
print(dig_pow(92, 1) == -1)
print(dig_pow(46288, 3) == 51)
print(dig_pow(695, 2) == 2)

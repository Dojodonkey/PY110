'''
A Rational Number is any number that can be represented as
the result of the division between two integers, e.g., 1/3, 3/2, 22/7, etc.
The number to the left is called the numerator,
and the number to the right is called the denominator.

A Unit Fraction is a rational number where the numerator is 1.

An Egyptian Fraction is the sum of a series of distinct unit fractions (no two are the same),
such as:

1   1    1    1
- + - + -- + --
2   3   13   15
Every positive rational number can be written as an Egyptian fraction. For example:

    1   1   1   1
2 = - + - + - + -
    1   2   3   6

Write two functions:
one that takes a Rational number as an argument,
and returns a list of the denominators that are part of an Egyptian Fraction representation of the number,
and another that takes a list of numbers in the same format, and calculates the resulting Rational number.
You will need to use the Fraction class provided by the fractions module.
'''

from fractions import Fraction

def egyptian(fractional_num):
    d = 1
    denominators = []
    remaining = fractional_num

    while remaining > 0:
        unit = Fraction(1, d)
        if unit <= remaining:
            denominators.append(d)
            remaining -= unit
        d += 1
    return denominators

def unegyptian(lst_of_denominators):
    # sum_ = 0
    # for denominator in lst_of_denominators:
    #     sum_ +=  Fraction(1, denominator)
    # return sum_
    return sum([Fraction(1, d) for d in lst_of_denominators])

# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))
'''
Every rational number can be expressed as an Egyptian Fraction.
In fact, every rational number can be expressed as an Egyptian Fraction in an infinite number of different ways.
Thus, the first group of examples may not show the same values as your solution.
They do, however, show the expected form of the solution.
The remaining examples merely demonstrate that the output of egyptian can be reversed by unegyptian.
'''
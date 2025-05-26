'''
# Write a function triple_double(num1, num2) which takes numbers num1 and num2
# and returns 1 if there is a straight triple of a number at any place in num1
# and also a straight double of the same number in num2. If this isn't the case,
# return 0
'''
def triple_double(num1, num2):
    str1 = str(num1)
    str2 = str(num2)

    for digit in str1:
        if digit * 3 in str1 and digit * 2 in str2:
            return 1

    return 0

print(triple_double(12345, 12345) == 0)
print(triple_double(666789, 12345667) == 1) # 3 straight 6's in num1, 2 straight 6's in num2)
print(triple_double(451999277, 41177722899) == 1)  # Triple 9, double 9
print(triple_double(1222345, 12345) == 0)  # Triple 2 but no double 2
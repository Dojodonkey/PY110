'''
problem statement:
Given the following data structure return a new list identical in structure to the original,
but containing only the numbers that are multiples of 3.
'''

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

def factor_3(a_lst):
    return [element for element in a_lst if element % 3 == 0]

lst_factors_of_3 = [factor_3(sub_list) for sub_list in lst]

print(lst_factors_of_3)
# expected result:
# [[], [3, 12], [9], [15, 18]]
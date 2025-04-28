'''
Problem Statement:
Given a dictionary, return its keys sorted by the values associated with each key.
'''
def item_value(item):
    return item[1]

def order_by_value(dictionary):
    sort_list = [item for item in dictionary.items()]
    sort_list.sort(key=item_value)
    return [key for key, value in sort_list]





my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
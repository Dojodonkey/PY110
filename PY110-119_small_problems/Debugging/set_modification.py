'''
We want to remove certain items from a set while iterating over it,
but the code below throws an error.
Why is that and how can we fix it?
'''
data_set = {1, 2, 3, 4, 5}

data_set = {num for num in data_set if num % 2 != 0}

print(data_set)

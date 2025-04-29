'''
You have a function that should check whether a key exists in a dictionary and returns its value.
However, it's raising an error. Why is that? How would you fix this code?
'''
# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))
# a KeyError is being thrown because 'b' is not a key in 'my_dict'.
# One solution would involve replacing the if/else block with a try/except block.
# def get_key_value(my_dict, key):
#     try:
#         if my_dict[key]:
#             return my_dict[key]
#     except KeyError:
#         return None

# print(get_key_value({"a": 1}, "b"))
# A better solution though would be using the dictionary method .get()
# which by default, returns None if the specified key is not found in a dictionary.
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))
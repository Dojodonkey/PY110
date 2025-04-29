'''
We have a list of lists and want to duplicate it.
After making the copy, we modify the original list,
but the copied list also seems to be affected:
'''
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original) # changed .copy attribute to .deepcopy

original[0][0] = 99

print(copied[0] == [1])
# the reason why shallow copies may affect original sequence objects is because only
# the top-most layer of elements are copied. All nested collections are stored in a
# different memory location and therefore element reassignment on those nested collections
# affect both the copy and the original object.
# To overcome this issue we must make a deep copy, which copies all elements, including nested collections.
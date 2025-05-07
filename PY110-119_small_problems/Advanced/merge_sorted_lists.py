'''
Write a function that takes two sorted lists as arguments and
returns a new list that contains all the elements from both input lists in ascending sorted order.
You may assume that the lists contain either all integer values or all string values.

You may not provide any solution that requires you to sort the result list.
You must build the result list one element at a time in the proper order.

Your solution should not mutate the input lists.

P:

- input: two lists
- output: a new list containing the two lists, in ascending order.

- explicit rules:
    - no sort functions.
    - output contains all elements of the merged two lists.
    - the two lists are both either integers or strings.
    - build the result list one element at a time.
- implicit rules: none

- questions: none

E:
```python
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])
```
D:

- List to merge the two lists.
- Another list containing the elements in ascending order.

A:

- High Level Strategy:
    - After merging the two lists, create a new list by iterating over the created one.
    If the element is greater than all the elements already in the list, it is appended to the back of the list.
    Otherwise it is appended after the last element that is less than it.

1. 'merged' is a list containing all elements from both input lists.
2. 'ordered' is initialized to an empty list.
3. iterate over merged.
    - if the element is greater than all elements already in the list, append it to the back.
    - if not, append it to the index before the element that it is less than.

C:
'''
def merge(lst1, lst2):
    merged = [*lst1, *lst2]
    asc_result = []

    for item in merged:
        if not asc_result:
            asc_result.append(item)
        else:
            inserted = False
            for i in range(len(asc_result)):
                if item < asc_result[i]:
                    asc_result.insert(i, item)
                    inserted = True
                    break
            if not inserted:
                asc_result.append(item)

    return asc_result

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)
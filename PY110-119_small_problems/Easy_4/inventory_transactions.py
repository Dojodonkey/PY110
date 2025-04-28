'''
Problem Statement:
Write a function that takes two arguments,
an inventory item ID and a list of transactions,
and returns a list containing only the transactions for the specified inventory item.

Understanding the Problem:

- input: integer and list
- output: list

- explicit rules:
    - the function takes 2 arguments, an id number and the list from which to refer to.
    - the output is a list containing only dictionaries regarding that 'id' number.
- implicit rules:
    - the list contains dictionaries.
    - each dictionary contains an 'id' number.
    - that entire dictionary should be returned to the list regarding the 'id' number.

- questions: none

Examples/Test Cases:

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

- understanding confirmed.

Data Structures:

- list for output value
- dictionaries as elements of the output list.

- High-Level Strategy:
    - create a list and then iterate over the input list. If the value mapped to 'id'
    is the same as the input integer, add the entire dictionary to the created list.

Algorithm:
1. create an empty list.
2. iterate over the list one element of a time.
3. if the value paired to 'id' is the same as the input integer, add it to the list.

Code:
'''
def transactions_for(id_num, lst):
    return [dictionary for dictionary in lst if dictionary['id'] == id_num]


transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True
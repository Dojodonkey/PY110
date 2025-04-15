# Building Blocks PEDAC excercise

## Understanding the Problem
- rules of a *valid structure*:
    - building blocks are cubes.
    - structure is built in *layers*.
    - the top-most layer is a single block.
    - a block in an upper layer *must* be supported by 4 blocks in a lower layer.
    - a block in a lower layer *can* support more than 1 block in an upper layer.
    - there are no gaps between blocks in the structure.

- input: number of available blocks.
- output: number of leftover blocks after building the tallest possible structure.

-explicit rules:
    - structure is built in layers.
    - top-most layer is a single block.
    - a block *must* be supported by ***4 blocks*** in the layer beneath it.
    - a block *can* support more than ***1 block*** in the layer above it.
        - visualize this in 3d. upper layers can overlap blocks of a lower layer.
    - there are no gaps of blocks within the layered structure.
- implicit rules:
    - an upper layer cannot have more than (lower layer) / 4 blocks in it.
    - the lower layers will contain the most blocks.
    - so beginning from the top layer (1), each row below it contains the previous row * 4.

## Test Cases / Examples
```python
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True / top-most block
print(calculate_leftover_blocks(2) == 1)  # True / top-most must be supported by 4
print(calculate_leftover_blocks(4) == 3)  # True / ''
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```
Confirms rules and understanding

## Data Structures

At this point, any ***mutable*** structure will do.
Thinking ***lists***.

## Algorithm
1. initialize a variable 'available cubes' referencing the amount of cubes available from the input.
    - the value will be modified throughout.
2. initialize an empty data structure, 'build' as a list ([]).
3. initialize a variable, 'layer number' referencing the amount of layers contained in the data structure.
    - as long as the input is not 0, there will be atleast 1 layer.
    - include margin test case to return 0 if input is 0.
4. as long as 'available cubes' is greater than 'layer number' squared:
    - initialize an empty 'layer' and append cubes based on 'layer number' squared.
        - append layer to 'build'
    - reassign 'available cubes' to 'available cubes' minus length of 'layer'.
    - reassign 'layer number' to 'layer number' + 1.
5. return the amount of available cubes left.

## Code
```python
def calculate_leftover_blocks(cubes):
    structure = []
    layer_number = 1

    while cubes >= layer_number ** 2:
        layer = []
        layer.append('x' * layer_number ** 2)
        structure.append(layer)
        cubes -= layer_number ** 2
        layer_number += 1

    return cubes

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True / top-most block
print(calculate_leftover_blocks(2) == 1)  # True / top-most must be supported by 4
print(calculate_leftover_blocks(4) == 3)  # True / ''
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True
```

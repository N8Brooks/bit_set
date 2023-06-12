# BitSet Implementation

This is a Python implementation of the `BitSet` class, which represents a collection of bits with _non-negative_ indexes.
The `BitSet` class provides various methods and operators for working with and manipulating bitsets.

## Installation

To use the `BitSet` implementation, you can copy the provided code into your project or use the code as reference.
It is not currently available on PyPi.
There are no additional dependencies required.

## Usage

Here is an overview of the main features and functionality of the `BitSet` class:

### Creating a BitSet

```py
bit_set = BitSet(bits)
```

To create a `BitSet` instance, you can pass the _bits_ argument, which represents the initial state of the bitset.
The _bits_ value should be a non-negative integer.

### Creating a BitSet from an Iterable

```py
bitset = BitSet.from_iter(iterable)
```

The `BitSet` class provides a static method `from_iter` that allows you to create a `BitSet` from an iterable object.
The iterable should contain non-negative integers, representing the bit indexes to be set in the `BitSet`.

### Setting a Bit

```py
bitset = BitSet.from_index(index)
```

You can create a `BitSet` with a specific bit index set to 1 using the `from_index` static method.

### Copying a BitSet

```py
new_bitset = bitset.copy()
```

The copy method creates a copy of the `BitSet` instance, allowing you to work with a separate instance.

### Iterating over Set Bits

```py
for bit_index in bitset:
    print(bit_index)
```

You can iterate over the 1 bits in the `BitSet` using a for loop.
The iteration will provide the bit indexes in ascending order.

### Reversed Iteration

```py
for bit_index in reversed(bitset):
    print(bit_index)
```

The reversed method enables reversed iteration over the 1 bits in the `BitSet`, providing the bit indexes in descending order.

### Checking a Bit for Membership

```py
if index in bitset:
    print("Bit is present")
```

You can use the in operator to check if a specific bit index is set in the `BitSet`.

## Set Operations

The `BitSet` class supports several set operations, including union, intersection, difference, and symmetric difference.

### Union:

```py
new_bitset = bitset.union(other_bitset1, other_bitset2, ...)
```

### Intersection:

```py
new_bitset = bitset.intersection(other_bitset1, other_bitset2, ...)
```

### Difference:

```py
new_bitset = bitset.difference(other_bitset1, other_bitset2, ...)
```

### Symmetric Difference:

```py
new_bitset = bitset.symmetric_difference(other_bitset)
```

## Comparison Operators

The `BitSet` class supports comparison operators for subset, superset, proper subset, and proper superset checks.

### Subset:

```py
if bitset <= other_bitset:
    print("BitSet is a subset")
```

### Superset:

```py
if bitset >= other_bitset:
    print("BitSet is a superset")
```

### Proper Subset:

```py
if bitset < other_bitset:
    print("BitSet is a proper subset")
```

### Proper Superset:

```py
if bitset > other_bitset:
    print("BitSet is a proper superset")
```

"""Testing for `BitSet` implementation"""
from itertools import product

import pytest

from bit_set.bit_set import BitSet

# pylint: disable=invalid-name,missing-function-docstring


def test_init_negative():
    with pytest.raises(Exception, match="must be non-negative"):
        BitSet(-1)


def test_from_bits():
    iterable = [1, 3]
    bit_set = BitSet.from_iter(iterable)
    assert bit_set.bits == 0b1010


def test_from_bits_negative():
    with pytest.raises(Exception, match="negative shift count"):
        BitSet.from_iter([-1])


def test_from_index():
    index = 3
    expected = 0b1000
    bit_set = BitSet.from_index(index)
    assert bit_set.bits == expected


def test_from_index_negative():
    with pytest.raises(Exception, match="negative shift count"):
        BitSet.from_index(-1)


def test_copy():
    bits = 0b1010
    bit_set = BitSet(bits).copy()
    assert bit_set.bits == bits


def test_bits():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert bit_set.bits == bit_set.bits == bits


def test_iter():
    expected = [1, 3]
    bit_set = BitSet.from_iter(expected)
    actual = list(bit_set)
    assert actual == expected


def test_reversed():
    expected = [3, 1]
    bit_set = BitSet.from_iter(expected)
    actual = list(reversed(bit_set))
    assert actual == expected


def test_len():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert len(bit_set) == 2


def test_contains():
    bits = {1, 3}
    bit_set = BitSet.from_iter(bits)
    for i in bits:
        assert i in bit_set
    for i in set(range(10)) - bits:
        assert i not in bit_set


def test_eq():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert (a == b) == (set(a) == set(b))


def test_ne():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert (a != b) == (set(a) != set(b))


def test_isdisjoint():
    a = BitSet(0b1010)
    b = BitSet(0b0101)
    assert a.isdisjoint(b)
    assert b.isdisjoint(a)


def test_not_isdisjoint():
    a = BitSet(0b1010)
    b = BitSet(0b1000)
    assert not a.isdisjoint(b)
    assert not b.isdisjoint(a)


def test_issubset():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert a.issubset(b) == set(a).issubset(set(b))


def test_lt():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert (a < b) == (set(a) < set(b))


def test_issuperset():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert a.issuperset(b) == set(a).issuperset(set(b))


def test_gt():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        assert (a > b) == (set(a) > set(b))


def test_hash():
    bits = 123
    bit_set = BitSet(bits)
    assert hash(bit_set) == hash(bits)


def test_str():
    bits = 123
    bit_set = BitSet(bits)
    assert str(bit_set) == bin(bits)


def test_union_two():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a).union(set(b))).bits
        assert a.union(b).bits == expected


def test_union_multiple():
    bits = 0b1010
    bit_set = BitSet(bits)
    for r in range(4):
        others = [BitSet(bits)] * r
        assert bit_set.union(*others).bits == bits


def test_or():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a) | set(b)).bits
        assert (a | b).bits == expected


def test_intersection_one():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert bit_set.intersection().bits == bits


def test_intersection_two():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a).intersection(set(b))).bits
        assert a.intersection(b).bits == expected


def test_intersection_multiple():
    bits_1 = 0b1010
    bits_2 = 0b0111
    expected = bits_1 & bits_2
    bit_set = BitSet(bits_1)
    for r in range(1, 4):
        others = [BitSet(bits_2)] * r
        assert bit_set.intersection(*others).bits == expected


def test_and():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a) & set(b)).bits
        assert (a & b).bits == expected


def test_difference_one():
    bits = 0b1111
    bit_set = BitSet(bits)
    assert bit_set.difference().bits == bits


def test_difference_two():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a).difference(set(b))).bits
        assert a.difference(b).bits == expected


def test_difference_multiple():
    bits_1 = 0b1010
    bits_2 = 0b0111
    expected = 0b1000
    bit_set = BitSet(bits_1)
    for r in range(1, 4):
        others = [BitSet(bits_2)] * r
        assert bit_set.difference(*others).bits == expected


def test_sub():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a) - set(b)).bits
        assert (a - b).bits == expected


def test_symmetric_difference():
    for a, b in product(map(BitSet, range(4)), repeat=2):
        expected = BitSet.from_iter(set(a).symmetric_difference(set(b))).bits
        assert a.symmetric_difference(b).bits == expected

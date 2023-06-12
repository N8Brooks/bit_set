"""Test"""
from bit_set.bit_set import BitSet


def test_init():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert bit_set._bits == bits


def test_from_bits():
    iterable = [1, 3]
    bit_set = BitSet.from_bits(iterable)
    assert bit_set._bits == 0b1010


def test_copy():
    bits = 0b1010
    bit_set = BitSet(bits).copy()
    assert bit_set.bits == bits


def test_bits():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert bit_set.bits == bit_set._bits == bits


def test_iter():
    expected = [1, 3]
    bit_set = BitSet.from_bits(expected)
    actual = list(bit_set)
    assert actual == expected


def test_reversed():
    expected = [3, 1]
    bit_set = BitSet.from_bits(expected)
    actual = list(reversed(bit_set))
    assert actual == expected


def test_len():
    bits = 0b1010
    bit_set = BitSet(bits)
    assert len(bit_set) == 2


def test_contains():
    bits = {1, 3}
    bit_set = BitSet.from_bits(bits)
    for i in bits:
        assert i in bit_set
    for i in set(range(10)) - bits:
        assert i not in bit_set

"""BitSet"""

from __future__ import annotations

from typing import Iterable

# pylint: disable=protected-access


class BitSet:
    """Represents a collection of **non-negative** bits."""

    def __init__(self, bits: int):
        self._bits = bits

    @staticmethod
    def from_iter(iterable: Iterable[int]) -> BitSet:
        """Returns a new `BitSet` whose elements are taken from iterable."""
        bits = 0
        for i in iterable:
            bits |= 1 << i
        return BitSet(bits)

    @staticmethod
    def from_index(i: int) -> BitSet:
        """Returns a `BitSet` with the given index, *i*, set to 1."""
        return BitSet(1 << i)

    def copy(self) -> BitSet:
        """Returns a copy of the `BitSet`."""
        return BitSet(self._bits)

    @property
    def bits(self) -> int:
        """Returns a copy of the bits in the `BitSet`."""
        return self._bits

    def __iter__(self) -> Iterable[int]:
        """An iterator of bits of the `BitSet` in ascending order."""
        n = self._bits.bit_length()  # pylint: disable=invalid-name
        return (i for i in range(n) if (1 << i) & self._bits)

    def __reversed__(self) -> Iterable[int]:
        """An iterator of bits of the `BitSet` in descending order."""
        n = self._bits.bit_length()  # pylint: disable=invalid-name
        return (i for i in reversed(range(n)) if (1 << i) & self._bits)

    def __len__(self) -> int:
        """Return the number of elements in the `BitSet`."""
        return self._bits.bit_count()

    def __contains__(self, i) -> bool:
        """Test *i* for membership in the `BitSet`."""
        return (1 << i) & self._bits != 0

    def isdisjoint(self, other: BitSet) -> bool:
        """Returns `True` if the `BitSet` has no elements in common with *other*."""
        return self._bits & other._bits == 0

    def issubset(self, other: BitSet) -> bool:
        """Test whether every element of the `BitSet` is in *other*."""
        return self <= other

    def __le__(self, other: BitSet) -> bool:
        """Test whether every element of the `BitSet` is in *other*."""
        return self._bits & other._bits == self._bits

    def __lt__(self, other: BitSet) -> bool:
        """Test whether the `BitSet` is a proper subset of *other*."""
        return self._bits != other._bits and self._bits & other._bits == self._bits

    def issuperset(self, other: BitSet) -> bool:
        """Test whether every element in *other* is in the `BitSet`."""
        return self >= other

    def __ge__(self, other: BitSet) -> bool:
        """Test whether every element in *other* is in the `BitSet`."""
        return self._bits & other._bits == other._bits

    def __gt__(self, other: BitSet) -> bool:
        """Test whether the `BitSet` is a proper superset of *other*."""
        return self._bits != other._bits and self._bits & other._bits == other._bits

    def __hash__(self) -> int:
        """Return the hash value of the `BitSet`."""
        return hash(self._bits)

    def __str__(self) -> str:
        """Converts the integer of the `BitSet` into its binary representation."""
        return bin(self._bits)

    def union(self, *others: BitSet) -> BitSet:
        """Return a new set with elements from the set and *other*."""
        bits = self._bits
        for other in others:
            bits |= other._bits
        return BitSet(bits)

    def __or__(self, other: BitSet) -> BitSet:
        """Return a new set with elements from the set and *other*."""
        return BitSet(self._bits | other._bits)

    def intersection(self, other) -> BitSet:
        """Return elements common to the `BitSet` and *other*."""
        return self & other

    def __and__(self, other: BitSet) -> BitSet:
        """Return a `BitSet` of elements common to the `BitSet` and *other*."""
        return BitSet(self._bits & other._bits)

    def difference(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with elements in the `BitSet` that are not in *other*."""
        return self - other

    def __sub__(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with elements in the `BitSet` that are not in *other*."""
        return BitSet(self._bits - (self._bits & other._bits))

    def symmetric_difference(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with elements in either the `BitSet` or *other*, but not both."""
        return self ^ other

    def __xor__(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with elements in either the `BitSet` or *other*, but not both."""
        return BitSet(self._bits ^ other._bits)

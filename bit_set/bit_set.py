"""BitSet implementation class"""

from __future__ import annotations

from typing import Iterable

# pylint: disable=protected-access


class BitSet:
    """Represents a collection of bits with **non-negative** indexes."""

    def __init__(self, bits: int):
        assert bits >= 0, "The `bits` argument must be non-negative."
        self._bits = bits

    @staticmethod
    def from_iter(iterable: Iterable[int]) -> BitSet:
        """Returns a new `BitSet` whose bit indexes are taken from *iterable*."""
        bits = 0
        for i in iterable:
            bits |= 1 << i
        return BitSet(bits)

    @staticmethod
    def from_index(*indexes: int) -> BitSet:
        """Returns a `BitSet` with each index set to 1."""
        return BitSet.from_iter(indexes)

    def copy(self) -> BitSet:
        """Returns a copy of this `BitSet`."""
        return BitSet(self._bits)

    @property
    def bits(self) -> int:
        """Returns a copy of `int` bits from this `BitSet`."""
        return self._bits

    def __iter__(self) -> Iterable[int]:
        """An iterator of the 1 bit indexes in ascending order."""
        n = self._bits.bit_length()  # pylint: disable=invalid-name
        return (i for i in range(n) if (1 << i) & self._bits)

    def __reversed__(self) -> Iterable[int]:
        """An iterator of the 1 bit indexes in descending order."""
        n = self._bits.bit_length()  # pylint: disable=invalid-name
        return (i for i in reversed(range(n)) if (1 << i) & self._bits)

    def __len__(self) -> int:
        """Return the count of 1 bits in this `BitSet`."""
        return self._bits.bit_count()

    def __contains__(self, i) -> bool:
        """Test the bit at index *i* for its membership in this `BitSet`."""
        return (1 << i) & self._bits != 0

    def isdisjoint(self, other: BitSet) -> bool:
        """Returns `True` if this `BitSet` has no bit in common with *other*."""
        return self._bits & other._bits == 0

    def issubset(self, other: BitSet) -> bool:
        """Test whether every bit of the `BitSet` is in *other*."""
        return self <= other

    def __le__(self, other: BitSet) -> bool:
        """Test whether every bit of this `BitSet` is in *other*."""
        return self._bits & other._bits == self._bits

    def __lt__(self, other: BitSet) -> bool:
        """Test whether this `BitSet` is a proper subset of *other*."""
        return self._bits != other._bits and self._bits & other._bits == self._bits

    def issuperset(self, other: BitSet) -> bool:
        """Test whether every bit in *other* is in this `BitSet`."""
        return self >= other

    def __ge__(self, other: BitSet) -> bool:
        """Test whether every bit in *other* is in this `BitSet`."""
        return self._bits & other._bits == other._bits

    def __gt__(self, other: BitSet) -> bool:
        """Test whether this `BitSet` is a proper superset of *other*."""
        return self._bits != other._bits and self._bits & other._bits == other._bits

    def __hash__(self) -> int:
        """Return the hash value of the `BitSet`."""
        return hash(self._bits)

    def __str__(self) -> str:
        """Converts the bits of this `BitSet` into its binary representation."""
        return bin(self._bits)

    def union(self, *others: BitSet) -> BitSet:
        """Return a new set with bits from this `BitSet` and *others*."""
        bits = self._bits
        for other in others:
            bits |= other._bits
        return BitSet(bits)

    def __or__(self, other: BitSet) -> BitSet:
        """Return a new set with bits from this `BitSet` and *other*."""
        return BitSet(self._bits | other._bits)

    def intersection(self, *others: BitSet) -> BitSet:
        """Return bits common to this `BitSet` and *others*."""
        bits = self._bits
        for other in others:
            bits &= other._bits
        return BitSet(bits)

    def __and__(self, other: BitSet) -> BitSet:
        """Return bits common to this `BitSet` and *other*."""
        return BitSet(self._bits & other._bits)

    def difference(self, *others: BitSet) -> BitSet:
        """Return a `BitSet` with bits from this `BitSet` that are not in *others*."""
        bits = self._bits
        for other in others:
            bits &= ~other._bits
        return BitSet(bits)

    def __sub__(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with bits from this `BitSet` that are not in *other*."""
        return BitSet(self._bits & ~other._bits)

    def symmetric_difference(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with bits in either this `BitSet` or *other*, but not both."""
        return self ^ other

    def __xor__(self, other: BitSet) -> BitSet:
        """Return a `BitSet` with bits in either this `BitSet` or *other*, but not both."""
        return BitSet(self._bits ^ other._bits)

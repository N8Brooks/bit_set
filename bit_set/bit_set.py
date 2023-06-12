"""BitSet"""

from __future__ import annotations

from typing import Iterable


class BitSet:
    def __init__(self, bits: int):
        self._bits = bits

    @staticmethod
    def from_iter(iterable: Iterable[int]) -> BitSet:
        bits = 0
        for i in iterable:
            bits |= 1 << i
        return BitSet(bits)

    def copy(self) -> BitSet:
        return BitSet(self._bits)

    @property
    def bits(self) -> int:
        return self._bits

    def __iter__(self) -> Iterable[int]:
        n = self._bits.bit_length()
        return (i for i in range(n) if (1 << i) & self._bits)

    def __reversed__(self) -> Iterable[int]:
        n = self._bits.bit_length()
        return (i for i in reversed(range(n)) if (1 << i) & self._bits)

    def __len__(self) -> int:
        return self._bits.bit_count()

    def __contains__(self, i) -> bool:
        return (1 << i) & self._bits != 0

    def __eq__(self, other: BitSet) -> bool:
        return self._bits == other._bits

    def __ne__(self, other: BitSet) -> bool:
        return self._bits != other._bits

    def isdisjoint(self, other: BitSet) -> bool:
        return self._bits & other._bits == 0

    def issubset(self, other: BitSet) -> bool:
        return self <= other

    def __le__(self, other: BitSet) -> bool:
        return self._bits & other._bits == self._bits

    def __lt__(self, other: BitSet) -> bool:
        return self._bits != other._bits and self._bits & other._bits == self._bits

    def issuperset(self, other: BitSet) -> bool:
        return self >= other

    def __ge__(self, other: BitSet) -> bool:
        return self._bits & other._bits == other._bits

    def __gt__(self, other: BitSet) -> bool:
        return self._bits != other._bits and self._bits & other._bits == other._bits

    def __hash__(self) -> int:
        return hash(self._bits)

    def __str__(self) -> str:
        return bin(self._bits)

    def union(self, other: BitSet) -> BitSet:
        return self | other

    def __or__(self, other: BitSet) -> BitSet:
        return BitSet(self._bits | other._bits)

    def intersection(self, other) -> BitSet:
        return self & other

    def __and__(self, other: BitSet) -> BitSet:
        return BitSet(self._bits & other._bits)

    def difference(self, other: BitSet) -> BitSet:
        return self - other

    def __sub__(self, other: BitSet) -> BitSet:
        return BitSet(self._bits - (self._bits & other._bits))

    def symmetric_difference(self, other: BitSet) -> BitSet:
        return self ^ other

    def __xor__(self, other: BitSet) -> BitSet:
        return BitSet(self._bits ^ other._bits)

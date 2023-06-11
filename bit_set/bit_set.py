"""BitSet"""

from __future__ import annotations

from typing import Iterable


class BitSet:
    def __init__(self, bits: int):
        self.bits = bits

    @staticmethod
    def from_bits(iterable: Iterable[int]) -> BitSet:
        bits = 0
        for i in iterable:
            bits |= 1 << i
        return BitSet(bits)

    def __iter__(self) -> Iterable[int]:
        n = self.bits.bit_length()
        return (i for i in range(n) if (1 << i) & self.bits)

    def __reversed__(self) -> Iterable[int]:
        n = self.bits.bit_length()
        return (i for i in reversed(range(n)) if (1 << i) & self.bits)

    def __len__(self) -> int:
        return self.bits.bit_count()

    def __contains__(self, i) -> bool:
        return bool((1 << i) & self.bits)

    def isdisjoint(self, other: BitSet) -> bool:
        return self.bits & other.bits == 0

    def issubset(self, other: BitSet) -> bool:
        return self <= other

    def __le__(self, other: BitSet) -> bool:
        raise NotImplementedError

    def __lt__(self, other: BitSet) -> bool:
        raise NotImplementedError

    def issuperset(self, other: BitSet) -> bool:
        return self >= other

    def __ge__(self, other: BitSet) -> bool:
        raise NotImplementedError

    def union(self, other: BitSet) -> BitSet:
        return self | other

    def __or__(self, other: BitSet) -> BitSet:
        return BitSet(self.bits | other.bits)

    def intersection(self, other) -> BitSet:
        return self & other

    def __and__(self, other: BitSet) -> BitSet:
        return BitSet(self.bits & other.bits)

    def difference(self, other: BitSet) -> BitSet:
        return self - other

    def __sub__(self, other: BitSet) -> BitSet:
        return BitSet(self.bits - (self.bits & other.bits))

    def symmetric_difference(self, other: BitSet) -> BitSet:
        return self ^ other

    def __xor__(self, other: BitSet) -> BitSet:
        return BitSet(self.bits ^ other.bits)

    def copy(self) -> BitSet:
        return BitSet(self.bits)

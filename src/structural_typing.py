from collections.abc import Iterable
from typing import Protocol, TypeVar

Number = TypeVar("Number", float, int)


class Operation(Protocol):
    @classmethod
    def apply(cls, a: Number, b: Number) -> Number:
        ...


def apply_to_all(operation: Operation, values: Iterable[Number]) -> Number:
    it = iter(values)
    value = next(it)

    for x in it:
        value = operation.apply(value, x)

    return value

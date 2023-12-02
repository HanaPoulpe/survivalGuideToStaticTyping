from collections.abc import Generator, Iterable
from typing import TypeVar

T = TypeVar("T")

def one_every_two_objects(source: Iterable[T]) -> Generator[T, None, None]: ...
def make_list(value: T) -> list[T]: ...

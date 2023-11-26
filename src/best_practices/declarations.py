from collections.abc import Generator, Iterable
from typing import TypeVar

T = TypeVar("T")


# def one_every_two_objects[T](source: list[T]) -> Generator[T, None, None]:
# Would create mypy errors for using the function with anything but a string
def one_every_two_objects(source: Iterable[T]) -> Generator[T, None, None]:
    for i, x in enumerate(source):
        if i % 2:
            continue

        yield x


# def make_list[T](value: T) -> Iterable[T]:
# Would create mypy errors if you try to append any values to the return value
def make_list(value: T) -> list[T]:
    return [value]


if __name__ == "__main__":
    for v in one_every_two_objects(range(10)):
        print(f"{v=}")

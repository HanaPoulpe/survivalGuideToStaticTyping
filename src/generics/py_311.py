from typing import Generic, TypeVar

# This demonstrates how to use TypeVar and Generics with type union
Number = TypeVar("Number", int, float)


class Addition(Generic[Number]):
    @classmethod
    def apply(cls, a: Number, b: Number) -> Number:
        return a + b


# This is an example of using TypeVar with inheritance
class MyClass:
    pass


AnyClass = TypeVar("AnyClass", bound=MyClass)

if __name__ == "__main__":
    result = Addition.apply(1, 2)  # Result is expected of type int
    print(f"{result=}")

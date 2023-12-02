from typing import Generic, TypeVar

Number = TypeVar("Number", int, float)

class Addition(Generic[Number]):
    @classmethod
    def apply(cls, a: Number, b: Number) -> Number: ...

class MyClass: ...

AnyClass = TypeVar("AnyClass", bound=MyClass)

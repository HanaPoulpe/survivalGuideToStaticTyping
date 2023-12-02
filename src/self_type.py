from typing import Self, TypeVar


class Vehicle:
    @classmethod
    def create_instance(cls: type[Self]) -> Self:
        return cls()


class Car(Vehicle):
    def __init__(self) -> None:
        self.engine = "fuel"


class Bicycle(Vehicle):
    pass


_V = TypeVar("_V", bound=Vehicle)


def create_vehicle(kind: type[_V]) -> _V:
    return kind.create_instance()


if __name__ == "__main__":
    car = create_vehicle(Car)
    print(car.engine)

    bicycle = create_vehicle(Bicycle)
    bicycle.engine  # Typing Error

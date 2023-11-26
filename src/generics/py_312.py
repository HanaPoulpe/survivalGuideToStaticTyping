Number = int | float


class Addition[T: Number]:
    @classmethod
    def apply(cls, a: T, b: T) -> T:
        return a + b


def add[T: Number](a: T, b: T) -> Number:
    return a + b


if __name__ == "__main__":
    result = Addition.apply(1, 2)  # Result is expected of type int
    print(f"{result=}")

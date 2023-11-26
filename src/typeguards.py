from typing import TypeGuard


def is_str_list(values: list) -> TypeGuard[list[str]]:
    return all(isinstance(v, str) for v in values)


def join_all(values: list) -> str:
    if not is_str_list(values):
        raise TypeError()

    return " ".join(values)


def upper(a: object) -> str:
    assert isinstance(a, str)
    return a.upper()

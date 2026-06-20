from typing import Callable, TypeVar

T = TypeVar("T")
U = TypeVar("U")

def map(iterable: list[T], func: Callable[[T], U]) -> list[U]:
    return [func(item) for item in iterable]

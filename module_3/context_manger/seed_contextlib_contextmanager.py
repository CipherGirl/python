import random
from contextlib import contextmanager
from typing import Iterator

@contextmanager
def seed(a: int | float | str | bytearray | None = None) -> Iterator[None]:
    random.seed(a)
    try:
        print("Yielding")
        yield
    finally:
        print("Resetting Seed")
        random.seed()


# def random_numbers(n: int = 3) -> list[int]:
    # return [random.randint(1, 10) for _ in range(n)]

# with seed(42):
#     print(random.random())
@seed(42)
def random_numbers(n: int = 3) -> list[int]:
    return [random.randint(1, 10) for _ in range(n)]



print(random_numbers())
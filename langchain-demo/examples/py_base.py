from copy import replace  # available: py >= 3.13
from dataclasses import dataclass

# demo: dataclass


@dataclass(frozen=True, kw_only=True)
class Point:
    x: int = 0
    y: int = 0


def test_update_immutable_dataclass():
    p = Point(x=1, y=2)
    p_moved = replace(p, x=10)
    print(f"p={p}, p_moved={p_moved}")


if __name__ == "__main__":
    test_update_immutable_dataclass()

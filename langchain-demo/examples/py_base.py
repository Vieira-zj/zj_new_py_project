from copy import replace  # available: py >= 3.13
from dataclasses import dataclass

from pydantic import SecretStr
from rich.console import Console


def call_package_fn():
    from langchain_base import langchain_help

    langchain_help()


def test_secret_str():
    console = Console()
    s = SecretStr("hello")
    console.print(f"secret string: [bold red]{s.get_secret_value()}[/bold red]")


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
    call_package_fn()
    # test_secret_str()
    # test_update_immutable_dataclass()

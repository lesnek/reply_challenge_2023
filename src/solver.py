from dataclasses import dataclass
from typing import Literal

from .model import Input


@dataclass
class Output:
    ...

Direction = Literal["L", "R", "D", "U"]
Position = tuple[int, int]
PortDirection = tuple[Direction, Position]

Snake = list[Direction | PortDirection]


@dataclass(frozen=True)
class State:
    matrix: list[list[int | Literal["*", "x"]]]
    available_snakes: list[int]
    snakes: list[Snake]


def solve(input: Input) -> Output:
    raise NotImplemented


def input_to_state(input: Input) -> State:
    raise NotImplemented

def get_available_positions() -> Output:
    raise NotImplemented

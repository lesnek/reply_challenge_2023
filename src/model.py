from typing import Literal
from dataclasses import dataclass


@dataclass
class Input:
    width: int
    heigth: int
    snakes_cnt: int
    snakes: list[int]
    matrix: list[list[int | Literal["*"]]]


@dataclass
class Output:
    ...


Direction = Literal["L", "R", "D", "U"]
Position = tuple[int, int]
PortDirection = tuple[Direction, Position]

SnakeSegments = list[Direction | PortDirection]


@dataclass(frozen=True)
class State:
    matrix: list[list[int | Literal["*", "x"]]]
    available_snakes: list[int]
    snakes: SnakeSegments


@dataclass
class CurrentSnake:
    remaining_segments: int
    assigned_segments: SnakeSegments

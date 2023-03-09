from collections.abc import Sequence
from typing import Literal
from dataclasses import dataclass


@dataclass
class Input:
    width: int
    heigth: int
    snakes_cnt: int
    snakes: Sequence[int]
    matrix: Sequence[Sequence[int | Literal["*"]]]


Direction = Literal["L", "R", "D", "U"]
Position = tuple[int, int]
PortDirection = tuple[Direction, Position]

SnakeSegments = Sequence[Direction | PortDirection]


@dataclass
class Output:
    snake_segments: Sequence[SnakeSegments]


@dataclass(frozen=True)
class State:
    matrix: Sequence[Sequence[int | Literal["*", "x"]]]
    available_snakes: Sequence[int]
    snakes: SnakeSegments


@dataclass
class CurrentSnake:
    remaining_segments: int
    assigned_segments: SnakeSegments

from collections.abc import Sequence
from typing import Literal
from dataclasses import dataclass

Position = tuple[int, int]  # = (row index, column index)


@dataclass
class Input:
    width: int
    heigth: int
    snakes_cnt: int
    snakes: Sequence[int]
    matrix: Sequence[Sequence[int | Literal["*"]]]
    portal_positions: Sequence[Position]


Direction = Literal["L", "R", "D", "U"]
PortDirection = tuple[Direction, Position]

SnakeSegments = tuple[
    Position, Sequence[Direction | PortDirection]
]  # = (starting position, directions)


@dataclass
class Output:
    snake_segments: Sequence[SnakeSegments]


@dataclass(frozen=True)
class State:
    matrix: list[list[int | Literal["*", "x"]]]
    available_snakes: Sequence[int]
    snakes: list[SnakeSegments]


@dataclass
class CurrentSnake:
    remaining_segments: int
    assigned_segments: SnakeSegments
    last_segment_position: Position

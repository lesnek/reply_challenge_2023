from typing import Literal
from dataclasses import dataclass


@dataclass
class Input:
    width: int
    heigth: int
    snakes_cnt: int
    snakes: list[int]
    matrix: list[list[int|Literal["*"]]]

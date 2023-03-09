from typing import Sequence, Literal

import pytest

from src.model import CurrentSnake, State, Position
from src.parser import InputParser
from src.solver import get_available_positions, get_best_position

EXAMPLE_INPUT = """10 6 5
6 7 5 3 3
1 5 3 6 3 8 5 2 6 8
6 4 * 0 5 3 7 5 2 8
3 4 5 0 3 6 4 * 5 7
3 5 6 3 0 3 5 3 4 6
3 6 7 * 3 0 6 4 5 7
3 7 8 5 3 6 0 4 5 6
"""


"""
    0 1 2 3 4 5 6 7 8 0
    -------------------
0 | 1 5 3 6 3 8 5 2 6 8
1 | 6 4 * 0 5 3 7 5 2 8
2 | 3 4 5 0 3 6 4 * 5 7
3 | 3 5 6 3 0 3 5 3 4 6
4 | 3 6 7 * 3 0 6 4 5 7
5 | 3 7 8 5 3 6 0 4 5 6
"""


def test_available_positions() -> None:
    parser = InputParser()
    input = parser.parse(EXAMPLE_INPUT)
    input.portal_positions = [(1, 2), (2, 7), (4, 3)]

    state = State(matrix=input.matrix, available_snakes=[], snakes=[])
    current_snake = CurrentSnake(
        remaining_segments=10, assigned_segments=[], last_segment_position=(1, 1)
    )

    available_positions = get_available_positions(input, state, current_snake)

    expected_available_positions = [
        ((0, 1), 1),
        ((2, 1), 1),
        ((1, 0), 1),
        ((1, 7), 2),
        ((2, 6), 2),
        ((2, 8), 2),
        ((3, 7), 2),
        ((3, 3), 2),
        ((4, 2), 2),
        ((5, 3), 2),
        ((4, 4), 2),
    ]

    assert set(available_positions) == set(expected_available_positions)


def test_available_positions_with_assigned_fields() -> None:
    parser = InputParser()
    input = parser.parse(EXAMPLE_INPUT)
    input.portal_positions = [(1, 2), (2, 7), (4, 3)]

    matrix = [
        [1, 5, 3, 6, 3, 8, 5, 2, 6, 8],
        [6, 4, "*", 0, 5, 3, 7, 5, 2, 8],
        [3, "x", 5, 0, 3, 6, 4, "*", "x", 7],
        [3, 5, 6, 3, 0, 3, 5, 3, 4, 6],
        [3, 6, 7, "*", 3, 0, 6, 4, 5, 7],
        [3, 7, 8, "x", 3, 6, 0, 4, 5, 6],
    ]
    state = State(matrix=matrix, available_snakes=[], snakes=[])
    current_snake = CurrentSnake(
        remaining_segments=10, assigned_segments=[], last_segment_position=(1, 1)
    )

    available_positions = get_available_positions(input, state, current_snake)

    expected_available_positions = [
        ((0, 1), 1),
        ((1, 0), 1),
        ((1, 7), 2),
        ((2, 6), 2),
        ((3, 7), 2),
        ((3, 3), 2),
        ((4, 2), 2),
        ((4, 4), 2),
    ]

    assert set(available_positions) == set(expected_available_positions)


@pytest.mark.parametrize(
    "matrix, best_coor",
    [
        (
            [
                [1, 5, 3, 6, 3, 8, 5, 2, 6, 8],
                [6, 4, "*", 0, 5, 3, 7, 5, 2, 8],
                [3, "x", 5, 0, 3, 6, 4, "*", "x", 7],
                [3, 5, 6, 3, 0, 3, 5, 3, 4, 6],
                [3, 6, 7, "*", 3, 0, 6, 4, 5, 7],
                [3, 7, 8, "x", 3, 6, 0, 4, 5, 6],
            ],
            (0, 5),
        ),
        (
            [
                [1, 5, 3, 6, 3, "X", 5, 2, 6, 8],
                [6, 4, "*", 0, 5, 3, 7, 5, 2, 8],
                [3, "x", 5, 0, 3, 6, 4, "*", "x", 7],
                [3, 5, 6, 3, 0, 3, 5, 3, 4, 6],
                [3, 6, 7, "*", 3, 0, 6, 4, 5, 7],
                [3, 7, 8, "x", 3, 6, 0, 4, 5, 6],
            ],
            (0, 9),
        ),
    ],
)
def test_best_position(
    matrix: Sequence[Sequence[int | Literal["*", "x"]]], best_coor: Position
):
    state = State(matrix=matrix, available_snakes=[], snakes=[])
    assert get_best_position(state) == best_coor

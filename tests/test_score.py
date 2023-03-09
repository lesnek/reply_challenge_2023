from src.model import State
from src.parser import InputParser
from src.score import calc_score
from copy import deepcopy

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


def test_calc_score() -> None:
    parser = InputParser()
    input = parser.parse(EXAMPLE_INPUT)

    state = State(matrix=deepcopy(input.matrix), available_snakes=[], snakes=[])
    assert calc_score(input, state) == 0

    assigmented = [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 9),
        (1, 1),
        (1, 3),
        (1, 4),
        (1, 5),
        (1, 6),
        (1, 7),
        (2, 8),
        (2, 9),
        (4, 2),
        (4, 4),
        (4, 5),
        (4, 6),
        (5, 8),
        (5, 9),
    ]
    for y, x in assigmented:
        state.matrix[y][x] = "x"
    assert calc_score(input, state) == 97

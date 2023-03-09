from src.parser import InputParser

EXAMPLE_INPUT = """10 6 5
6 7 5 3 3
1 5 3 6 3 8 5 2 6 8
6 4 * 0 5 3 7 5 2 8
3 4 5 0 3 6 4 * 5 7
3 5 6 3 0 3 5 3 4 6
3 6 7 * 3 0 6 4 5 7
3 7 8 5 3 6 0 4 5 6
"""


def test_input_parser() -> None:
    parser = InputParser()
    input = parser.parse(EXAMPLE_INPUT)

    assert input.width == 10
    assert input.heigth == 6
    assert input.snakes_cnt == 5
    assert input.snakes == [6, 7, 5, 3, 3]
    assert input.matrix == [
        [1, 5, 3, 6, 3, 8, 5, 2, 6, 8],
        [6, 4, "*", 0, 5, 3, 7, 5, 2, 8],
        [3, 4, 5, 0, 3, 6, 4, "*", 5, 7],
        [3, 5, 6, 3, 0, 3, 5, 3, 4, 6],
        [3, 6, 7, "*", 3, 0, 6, 4, 5, 7],
        [3, 7, 8, 5, 3, 6, 0, 4, 5, 6],
    ]

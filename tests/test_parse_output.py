from src.parser import OutputParser
from src.model import Output

EXAMPLE_OUTPUT = Output(
    snake_segments=[
        [0, 0, "R", "R", "D", 7, 2, "R", "R"],
        [6, 1, "L", "U", "L", "D", "L", "U"],
        [1, 1, "R", 3, 4, "R", "R", "R"],
        [7, 1, "D", 3, 4, "L"],
        [9, 0, "U", "L"],
    ]
)


def test_input_parser() -> None:
    parser = OutputParser()
    output = parser.parse(EXAMPLE_OUTPUT)

    assert (
        output
        == """0 0 R R D 7 2 R R
6 1 L U L D L U
1 1 R 3 4 R R R
7 1 D 3 4 L
9 0 U L"""
    )

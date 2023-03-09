from .model import Input, State


def calc_score(input: Input, state: State) -> int:
    return sum(
        [
            int(input.matrix[y][x])
            for x in range(input.width)
            for y in range(input.heigth)
            if state.matrix[y][x] == "x"
        ]
    )

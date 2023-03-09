from collections.abc import Sequence

from .model import CurrentSnake, Input, Output, Position, State


def solve(input: Input) -> Output:
    raise NotImplemented


def input_to_state(input: Input) -> State:
    return State(
        matrix=input.matrix,
        available_snakes=input.snakes,
        snakes=[],
    )


def get_near_positions(
    input: Input, state: State, position: Position
) -> Sequence[Position]:
    cur_row, cur_col = position

    positions = [
        (cur_row, (cur_col - 1) % input.width),
        (cur_row, (cur_col + 1) % input.width),
        ((cur_row - 1) % input.heigth, cur_col),
        ((cur_row + 1) % input.heigth, cur_col),
    ]

    return [
        position
        for position in positions
        if state.matrix[position[0]][position[1]] != "x"
    ]


def get_available_positions(
    input: Input, state: State, current: CurrentSnake
) -> Sequence[tuple[Position, int]]:
    """Returns available positions with number of segments it consumes."""

    matrix = state.matrix
    remaining_segments = current.remaining_segments

    assert remaining_segments > 0

    positions = get_near_positions(input, state, current.last_segment_position)

    final_positions = []

    for position in positions:
        value = matrix[position[0]][position[1]]

        if value == "x" or (value == "*" and remaining_segments < 2):
            continue
        elif value == "*":
            for portal_position in input.portal_positions:
                if portal_position == position:
                    continue

                portal_positions = get_near_positions(input, state, portal_position)
                final_positions.extend([(position, 2) for position in portal_positions])
        else:
            final_positions.append((position, 1))

    return final_positions

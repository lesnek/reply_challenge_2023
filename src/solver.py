from collections.abc import Sequence
from itertools import product
from typing import Literal, cast

from .model import (CurrentSnake, Direction, Input, Output, PortDirection,
                    Position, SnakeSegments, State)


def solve(input: Input) -> tuple[Output, State]:
    state = input_to_state(input)

    sorted_positions = sorted(
        [
            (r, c)
            for r, c in list(product(range(input.heigth), range(input.width)))
            if input.matrix[r][c] != "*"
        ],
        key=lambda x: (compare_positions(input.matrix))((x, 0)),
        reverse=True,
    )
    n = 0

    for i, snake_segments_cnt in enumerate(sorted(input.snakes, reverse=True)):
        result = None

        while result is None:
            first_position = get_best_position(state, n, sorted_positions)
            state.matrix[first_position[0]][first_position[1]] = "x"

            print(f"{i / len(input.snakes) * 100}%")

            snake = CurrentSnake(
                remaining_segments=snake_segments_cnt - 1,
                assigned_segments=(first_position, []),
                last_segment_position=first_position,
            )
            result = solve_snake(input, state, snake)
            n += 1

            if n >= len(input.snakes):
                n = 0

        state.snakes.append(result)

    return Output(snake_segments=state.snakes), state


def compare_positions(matrix: Sequence[Sequence[int | Literal["*"]]]):
    def compare(value):
        return matrix[value[0][0]][value[0][1]]
    return compare


def solve_snake(
    input: Input, state: State, snake: CurrentSnake
) -> SnakeSegments | None:
    if snake.remaining_segments == 0:
        return snake.assigned_segments

    available_positions = get_available_positions(input, state, snake)

    if len(available_positions) == 0:
        return None

    sorted_positions = sorted(
        available_positions, key=compare_positions(state.matrix), reverse=True # type: ignore
    )
    i = 0
    result = None

    while result is None:
        if i == len(sorted_positions):
            return None

        best_position, best_consumption, best_direction = sorted_positions[i]
        new_assigned_segments: list[Direction | PortDirection] = [
            i for i in snake.assigned_segments[1]
        ]  # copy
        new_assigned_segments.append(
            get_direction(snake.last_segment_position, best_position, best_direction)
        )

        new_snake = CurrentSnake(
            remaining_segments=snake.remaining_segments - best_consumption,
            assigned_segments=(snake.assigned_segments[0], new_assigned_segments),
            last_segment_position=best_position,
        )
        state.matrix[best_position[0]][best_position[1]] = "x"
        result = solve_snake(input, state, new_snake)
        i += 1

    return result


def get_direction(
    previous: Position, new: Position, direction: Direction
) -> Direction | PortDirection:
    row_diff, col_diff = previous[0] - new[0], previous[1] - new[1]

    if row_diff + col_diff <= 1:
        return direction
    else:
        return direction, new


def get_best_position(state: State, n: int, positions) -> Position:
    i = 0

    for row, col in positions:
        if i == n:
            return (row, col)

        if type(state.matrix[row][col]) == int:
            i += 1

    raise Exception("V prdeli")


def input_to_state(input: Input) -> State:
    return State(
        matrix=[[i for i in row] for row in input.matrix],  # type: ignore
        available_snakes=input.snakes,
        snakes=[],
    )


def get_near_positions(
    input: Input, state: State, position: Position
) -> Sequence[tuple[Position, Direction]]:
    cur_row, cur_col = position

    positions: list[tuple[Position, Direction]] = [
        ((cur_row, (cur_col - 1) % input.width), "L"),
        ((cur_row, (cur_col + 1) % input.width), "R"),
        (((cur_row - 1) % input.heigth, cur_col), "U"),
        (((cur_row + 1) % input.heigth, cur_col), "D"),
    ]

    return [
        position
        for position in positions
        if state.matrix[position[0][0]][position[0][1]] != "x"
    ]


def get_available_positions(
    input: Input, state: State, current: CurrentSnake
) -> Sequence[tuple[Position, int, Direction]]:
    """Returns available positions with number of segments it consumes."""

    matrix = state.matrix
    remaining_segments = current.remaining_segments

    assert remaining_segments > 0

    positions = get_near_positions(input, state, current.last_segment_position)

    final_positions = []

    for position, direction in positions:
        value = matrix[position[0]][position[1]]

        if value == "x" or (value == "*" and remaining_segments < 2):
            continue
        elif value == "*":
            for portal_position in input.portal_positions:
                if portal_position == position:
                    continue

                portal_positions = [
                    p[0]
                    for p in get_near_positions(input, state, portal_position)
                    if matrix[p[0][0]][p[0][1]] != "*"
                ]
                final_positions.extend([(p, 1, direction) for p in portal_positions])
        else:
            final_positions.append((position, 1, direction))

    return final_positions

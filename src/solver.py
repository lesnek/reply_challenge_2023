from collections.abc import Sequence
from typing import cast

from src.parser import OutputParser

from .model import (
    CurrentSnake,
    Direction,
    Input,
    Output,
    PortDirection,
    Position,
    SnakeSegments,
    State,
)


def solve(input: Input) -> tuple[Output, State]:
    state = input_to_state(input)

    for snake_segments_cnt in input.snakes:
        first_position = get_best_position(state)

        snake = CurrentSnake(
            remaining_segments=snake_segments_cnt - 1,
            assigned_segments=(first_position, []),
            last_segment_position=first_position,
        )
        snake_segments = solve_snake(input, state, snake)
        state.snakes.append(snake_segments)

    return Output(snake_segments=state.snakes), state


def solve_snake(input: Input, state: State, snake: CurrentSnake) -> SnakeSegments:
    if snake.remaining_segments == 0:
        return snake.assigned_segments

    available_positions = get_available_positions(input, state, snake)

    assert len(available_positions) > 0

    best_position, best_consumption, best_direction = available_positions[0]
    best_value = input.matrix[best_position[0]][best_position[1]]

    assert type(best_value) == int

    for new_position, new_consumption, new_direction in available_positions[1:]:
        new_value = input.matrix[new_position[0]][best_position[1]]

        assert type(new_value) == int

        if cast(int, new_value) > cast(int, best_value):
            best_position = new_position
            best_consumption = new_consumption
            best_value = new_value
            best_direction = new_direction

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
    return solve_snake(input, state, new_snake)


def get_direction(
    previous: Position, new: Position, direction: Direction
) -> Direction | PortDirection:
    row_diff, col_diff = previous[0] - new[0], previous[1] - new[1]

    if row_diff + col_diff <= 1:
        return direction
    else:
        return direction, new


def get_best_position(state: State) -> Position:
    best_value = 0
    best_coor = (0, 0)
    x, y = 0, 0
    for row in state.matrix:
        for value in row:
            if isinstance(value, int) and value > best_value:
                best_value = value
                best_coor = (y, x)
            x += 1
        y += 1

    return best_coor


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

    positions = [
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

                portal_positions = get_near_positions(input, state, portal_position)
                final_positions.extend(
                    [(position[0], 2, direction) for position in portal_positions]
                )
        else:
            final_positions.append((position, 1, direction))

    return final_positions

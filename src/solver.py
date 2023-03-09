from .model import CurrentSnake, Input, Output, Position, State


def solve(input: Input) -> Output:
    raise NotImplemented


def input_to_state(input: Input) -> State:
    return State(
        matrix=input.matrix,
        available_snakes=input.snakes,
        snakes=[],
    )


def get_available_positions(state: State, current: CurrentSnake) -> list[Position]:
    raise NotImplemented

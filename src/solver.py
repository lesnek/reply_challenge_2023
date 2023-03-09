from .model import Input, Output, Position, State


def solve(input: Input) -> Output:
    raise NotImplemented


def input_to_state(input: Input) -> State:
    return State(
        matrix=input.matrix,
        available_snakes=input.snakes,
        snakes=[],
    )



def get_available_positions(state: State) -> list[Position]:
    raise NotImplemented

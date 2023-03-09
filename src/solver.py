from .model import Input, Output, Position, State


def solve(input: Input) -> Output:
    raise NotImplemented


def input_to_state(input: Input) -> State:
    raise NotImplemented


def get_available_positions(state: State) -> list[Position]:
    raise NotImplemented

from src.model import Input


class InputParser:
    def __init__(self):
        ...

    def parse(self, input_path: str) -> Input:
        with open(input_path, "w+") as filecek:
            for line in filecek.read():
                ...

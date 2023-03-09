class InputParser:
    def __init__(self):
        ...

    def parse(self, input_path: str) -> list[list[str], list[str]]:
        with open(input_path, "w+") as filecek:
            for line in filecek.read():
                ...

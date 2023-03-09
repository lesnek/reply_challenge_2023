from typing import Literal, Sequence

from src.model import Input, Output


class InputParser:
    def __init__(self):
        ...

    def parse(self, input_string: str) -> Input:
        input_string = input_string.replace("\n\n", "\n")
        lines = [line.replace("\n", "") for line in input_string.split("\n")]
        width, heigth, snakes_cnt = [int(char) for char in lines[0].split(" ")]
        snakes = [int(snake) for snake in lines[1].split(" ")]
        matrix = []
        portal_positions = []
        x, y = 0, 0
        for line in lines[2:-1]:
            matrix.append(
                [self.parse_int_or_asterisk(char) for char in line.split(" ")]
            )
            if "*" in matrix[y]:
                portal_positions.extend(self.get_portal_positions(y, matrix[y]))
            y += 1

        return Input(
            width=width,
            heigth=heigth,
            snakes_cnt=snakes_cnt,
            snakes=snakes,
            matrix=matrix,
            portal_positions=portal_positions,
        )

    @staticmethod
    def get_portal_positions(
        y, row: Sequence[int | Literal["*"]]
    ) -> Sequence[tuple[int, int]]:
        result = []
        x_coor = 0
        for x in row:
            if x == "*":
                result.append((y, x_coor))
            x_coor += 1
        return result

    @staticmethod
    def parse_int_or_asterisk(char: str) -> int | Literal["*"]:
        if char == "*":
            return "*"
        return int(char)

    @staticmethod
    def open_file(path_to_file: str) -> str:
        with open(path_to_file, "r+") as filecek:
            lines = filecek.read()
        return lines


class OutputParser:
    @staticmethod
    def snake_seg_to_str(snake_segs) -> Sequence[str]:
        return [str(seg) for seg in snake_segs]

    @staticmethod
    def parse(output: Output) -> str:
        result = []
        for snake_segs in output.snake_segments:
            result.append(" ".join(OutputParser.snake_seg_to_str(snake_segs)))
        return "\n".join(result)

    @staticmethod
    def save_to_file(output: Output) -> None:
        with open("result.txt", "w+") as filecek:
            for snake_segs in output.snake_segments:
                filecek.write(" ".join(OutputParser.snake_seg_to_str(snake_segs)))

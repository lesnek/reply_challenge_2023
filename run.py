from argparse import ArgumentParser

from src.parser import InputParser, OutputParser
from src.score import calc_score
from src.solver import solve

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename")

    args = parser.parse_args()


    input_parser = InputParser()
    input_data = input_parser.open_file(args.filename)
    input = input_parser.parse(input_data)
    output, state = solve(input)
    print(f"{calc_score(input, state)=}")
    print(OutputParser.parse(output))
    


if __name__ == "__main__":
    main()

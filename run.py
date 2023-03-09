from argparse import ArgumentParser

from src.parser import InputParser
from src.solver import solve

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--filename")

    args = parser.parse_args()


    input_parser = InputParser()
    input_data = input_parser.open_file(args.filename)
    print(input_data)
    input = input_parser.parse(input_data)
    result = solve(input)
    print(result)


if __name__ == "__main__":
    main()

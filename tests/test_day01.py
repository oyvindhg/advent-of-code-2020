from src.day01 import parse_puzzle, solve_1, solve_2


def test_solutions():
    numbers = parse_puzzle('data/test/day01.txt')
    assert solve_1(numbers) == 514579
    assert solve_2(numbers) == 241861950

import time


def parse_puzzle(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def solve_1(data: list[str]) -> int:
    print(data)
    return 0


def solve_2(data: list[str]) -> int:
    print(data)
    return 0


def test_solutions():
    data = parse_puzzle('data/test/day01.txt')
    assert solve_1(data) == 1
    assert solve_2(data) == 1


def main():
    data = parse_puzzle('data/real/day01.txt')

    start_time = time.time()
    print('---Task 1---')
    print(f"Solution 1: {solve_1(data)}")
    print(f"Time: {time.time() - start_time:.4f} ms")
    print()

    start_time = time.time()
    print('---Task 2---')
    print(f"Solution 2: {solve_2(data)}")
    print(f"Time: {time.time() - start_time:.4f} ms")


if __name__ == '__main__':
    main()

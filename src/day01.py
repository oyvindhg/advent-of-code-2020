import time


def parse_puzzle(filename: str) -> list[int]:
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        return [int(item) for item in lines]


def solve_1(numbers: list[int]) -> int:
    number_count = len(numbers)
    for i in range(number_count):
        for j in range(i, number_count):
            if numbers[i] + numbers[j] == 2020:
                return numbers[i] * numbers[j]


def solve_2(numbers: list[int]) -> int:
    number_count = len(numbers)
    for i in range(number_count):
        for j in range(i, number_count):
            for k in range(j, number_count):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    return numbers[i] * numbers[j] * numbers[k]


def main():
    numbers = parse_puzzle('data/real/day01.txt')

    start_time = time.time()
    print('---Task 1---')
    print(f"Solution 1: {solve_1(numbers)}")
    print(f"Time: {time.time() - start_time:.4f} ms")
    print()
    
    start_time = time.time()
    print('---Task 2---')
    print(f"Solution 2: {solve_2(numbers)}")
    print(f"Time: {time.time() - start_time:.4f} ms")


if __name__ == '__main__':
    main()

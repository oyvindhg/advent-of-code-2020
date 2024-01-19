import time


def parse_puzzle(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def run_simulation(slope_map: list[str], right: int, down: int) -> int:
    x_pos = 0
    y_pos = 0
    slope_map_height = len(slope_map)
    slope_map_width = len(slope_map[0])
    trees_hit = 0

    while y_pos < slope_map_height:
        position_on_map = x_pos % slope_map_width
        if slope_map[y_pos][position_on_map] == '#':
            trees_hit += 1
        y_pos += down
        x_pos += right

    return trees_hit


def solve_1(slope_map: list[str]) -> int:
    return run_simulation(slope_map, 3, 1)


def solve_2(slope_map: list[str]) -> int:
    return (run_simulation(slope_map, 1, 1)
            * run_simulation(slope_map, 3, 1)
            * run_simulation(slope_map, 5, 1)
            * run_simulation(slope_map, 7, 1)
            * run_simulation(slope_map, 1, 2))


def test_solutions():
    slope_map = parse_puzzle('data/test/day03.txt')
    assert solve_1(slope_map) == 7
    assert solve_2(slope_map) == 336


def main():
    slope_map = parse_puzzle('data/real/day03.txt')

    start_time = time.time()
    print('---Task 1---')
    print(f"Solution 1: {solve_1(slope_map)}")
    print(f"Time: {time.time() - start_time:.4f} ms")
    print()

    start_time = time.time()
    print('---Task 2---')
    print(f"Solution 2: {solve_2(slope_map)}")
    print(f"Time: {time.time() - start_time:.4f} ms")


if __name__ == '__main__':
    main()

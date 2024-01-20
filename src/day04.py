import time


def parse_puzzle(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def is_valid_field(field: str, data: str) -> bool:
    match field:
        case 'byr':
            if len(data) == 4 and data.isdigit() and 1920 <= int(data) <= 2002:
                return True
        case 'iyr':
            if len(data) == 4 and data.isdigit() and 2010 <= int(data) <= 2020:
                return True
        case 'eyr':
            if len(data) == 4 and data.isdigit() and 2020 <= int(data) <= 2030:
                return True
        case 'hgt':
            if len(data) <= 2:
                return False
            if data[-2:] == 'cm':
                if 150 <= int(data[:-2]) <= 193:
                    return True
            if data[-2:] == 'in':
                if 59 <= int(data[:-2]) <= 76:
                    return True
        case 'hcl':
            if len(data) != 7:
                return False
            for character_number, character in enumerate(data):
                if character_number == 0:
                    if character != '#':
                        return False
                elif character not in '0123456789abcdef':
                    return False
            return True
        case 'ecl':
            if data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return True
        case 'pid':
            if len(data) == 9 and data.isdigit():
                return True
        case 'cid':
            return True
    return False


def find_valid_passports(passports: list[str], validate_fields: bool) -> int:
    valid_passports = 0

    expected_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    current_passport_fields = set()
    for passport_line in passports:
        if not passport_line:
            if expected_fields.issubset(current_passport_fields):
                valid_passports += 1
            current_passport_fields = set()

        data_fields = passport_line.split()
        for data_field in data_fields:
            field, data = data_field.split(':')
            if validate_fields:
                if is_valid_field(field, data):
                    current_passport_fields.add(field)
            else:
                current_passport_fields.add(field)

    if expected_fields.issubset(current_passport_fields):
        valid_passports += 1
    return valid_passports


def solve_1(passports: list[str]) -> int:
    return find_valid_passports(passports, False)


def solve_2(passports: list[str]) -> int:
    return find_valid_passports(passports, True)


def test_solutions():
    passports = parse_puzzle('data/test/day04.txt')
    assert solve_1(passports) == 2
    invalid_passports = parse_puzzle('data/test/day04-invalid.txt')
    valid_passports = parse_puzzle('data/test/day04-valid.txt')
    assert solve_2(invalid_passports) == 0
    assert solve_2(valid_passports) == 4


def main():
    passports = parse_puzzle('data/real/day04.txt')

    start_time = time.time()
    print('---Task 1---')
    print(f"Solution 1: {solve_1(passports)}")
    print(f"Time: {time.time() - start_time:.4f} ms")
    print()

    start_time = time.time()
    print('---Task 2---')
    print(f"Solution 2: {solve_2(passports)}")
    print(f"Time: {time.time() - start_time:.4f} ms")


if __name__ == '__main__':
    main()

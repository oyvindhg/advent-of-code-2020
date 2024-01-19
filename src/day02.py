import time
from dataclasses import dataclass


@dataclass
class Policy:
    lower: int
    upper: int
    letter: str


@dataclass
class PolicyPassword:
    policy: Policy
    password: str


def parse_puzzle(filename: str) -> list[PolicyPassword]:
    with open(filename, 'r') as f:
        rows = f.read().splitlines()

    policy_passwords = []
    for row in rows:
        policy_text, password = row.split(': ')
        boundaries, letter = policy_text.split()
        lower, upper = [int(number) for number in boundaries.split('-')]
        policy_passwords.append(
            PolicyPassword(
                policy=Policy(
                    lower=lower,
                    upper=upper,
                    letter=letter
                ),
                password=password
            )
        )
    return policy_passwords


def solve_1(policy_passwords: list[PolicyPassword]) -> int:
    valid_passwords_count = 0
    for policy_password in policy_passwords:
        letter_occurrences = 0
        for letter in policy_password.password:
            if letter == policy_password.policy.letter:
                letter_occurrences += 1
        if policy_password.policy.lower <= letter_occurrences <= policy_password.policy.upper:
            valid_passwords_count += 1
    return valid_passwords_count


def solve_2(policy_passwords: list[PolicyPassword]) -> int:
    valid_passwords_count = 0
    for policy_password in policy_passwords:
        lower_contains = policy_password.password[policy_password.policy.lower - 1] == policy_password.policy.letter
        upper_contains = policy_password.password[policy_password.policy.upper - 1] == policy_password.policy.letter
        if (lower_contains and not upper_contains) or (not lower_contains and upper_contains):
            valid_passwords_count += 1
    return valid_passwords_count


def test_solutions():
    numbers = parse_puzzle('data/test/day02.txt')
    assert solve_1(numbers) == 2
    assert solve_2(numbers) == 1


def main():
    policy_passwords = parse_puzzle('data/real/day02.txt')

    start_time = time.time()
    print('---Task 1---')
    print(f"Solution 1: {solve_1(policy_passwords)}")
    print(f"Time: {time.time() - start_time:.4f} ms")
    print()

    start_time = time.time()
    print('---Task 2---')
    print(f"Solution 2: {solve_2(policy_passwords)}")
    print(f"Time: {time.time() - start_time:.4f} ms")


if __name__ == '__main__':
    main()

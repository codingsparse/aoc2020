import re
from pathlib import Path

from collections import Counter


def is_count_valid(password, char, min, max):
    counter = Counter(password)
    num_char = counter.get(char, 0)
    return min <= num_char <= max


def is_position_valid(password, char, pos_a, pos_b):
    is_pos_a_valid = password[pos_a - 1] == char
    is_pos_b_valid = password[pos_b - 1] == char
    return (int(is_pos_a_valid) + int(is_pos_b_valid)) == 1


with open(Path(__file__).parent / "data" / "day02.txt", "r") as f:
    file_line_pattern = re.compile(r"([\d]+)-([\d]+) ([\w]{1}): ([\w]+)")
    num_valids = 0
    for line in f.readlines():
        match = re.search(file_line_pattern, line)
        min = int(match.group(1))
        max = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        num_valids += int(is_count_valid(password, char, min, max))
    print("First part (count)")
    print(f"Number of valid passwords: {num_valids}.")


with open(Path(__file__).parent / "data" / "day02.txt", "r") as f:
    file_line_pattern = re.compile(r"([\d]+)-([\d]+) ([\w]{1}): ([\w]+)")
    num_valids = 0
    for line in f.readlines():
        match = re.search(file_line_pattern, line)
        pos_a = int(match.group(1))
        pos_b = int(match.group(2))
        char = match.group(3)
        password = match.group(4)
        num_valids += int(is_position_valid(password, char, pos_a, pos_b))
    print("Second part (position based)")
    print(f"Number of valid passwords: {num_valids}.")

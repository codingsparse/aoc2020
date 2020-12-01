from pathlib import Path


def find_two_elements_that_sum_to_x(l: list, x: int) -> tuple([int, int]):
    for i in range(len(l)):
        a = l[i]
        for j in range(i + 1, len(l)):
            b = l[j]
            if a + b == x:
                return (a, b)


def find_three_elements_that_sum_to_x(l: list, x: int) -> tuple([int, int, int]):
    for i in range(len(l)):
        a = l[i]
        for j in range(i + 1, len(l)):
            b = l[j]
            for k in range(j + 1, len(l)):
                c = l[k]
                if a + b + c == x:
                    return (a, b, c)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        l = [int(i) for i in f.readlines()]
    x = 2020
    a, b = find_two_elements_that_sum_to_x(l, x)
    if a and b:
        print(f"Found elements {a} and {b} that sum to {x}.")
        print(f"They multiply to {a*b}.")
    a, b, c = find_three_elements_that_sum_to_x(l, x)
    if a and b and c:
        print(f"Found elements {a}, {b} and {c} that sum to {x}.")
        print(f"They multiply to {a*b*c}.")

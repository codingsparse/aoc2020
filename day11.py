def read_grid():
    return open("data/day11.txt").read().splitlines()


GRID = read_grid()
Y_LEN = len(GRID)
X_LEN = len(GRID[0])


def adjacents(x, y):
    up_left = GRID[y - 1][x - 1] if x > 0 and y > 0 else "."
    up = GRID[y - 1][x] if y > 0 else "."
    up_right = GRID[y - 1][x + 1] if y > 0 and x + 1 < X_LEN else "."
    left = GRID[y][x - 1] if x > 0 else "."
    right = GRID[y][x + 1] if x + 1 < X_LEN else "."
    down_left = GRID[y + 1][x - 1] if y + 1 < Y_LEN and x > 0 else "."
    down = GRID[y + 1][x] if y + 1 < Y_LEN else "."
    down_right = GRID[y + 1][x + 1] if y + 1 < Y_LEN and x + 1 < X_LEN else "."
    return [up_left, up, up_right, left, right, down_left, down, down_right]


def find_visible(x, y, rule):
    new_x, new_y = x, y
    visible_seat = "."
    while (
        0 <= new_x + rule[0] < X_LEN
        and 0 <= new_y + rule[1] < Y_LEN
        and visible_seat == "."
    ):
        new_x = new_x + rule[0]
        new_y = new_y + rule[1]
        visible_seat = GRID[new_y][new_x]
    return visible_seat


def visible(x, y):
    up_left = find_visible(x, y, rule=(-1, -1))
    up = find_visible(x, y, rule=(0, -1))
    up_right = find_visible(x, y, rule=(1, -1))
    left = find_visible(x, y, rule=(-1, 0))
    right = find_visible(x, y, rule=(1, 0))
    down_left = find_visible(x, y, rule=(-1, 1))
    down = find_visible(x, y, rule=(0, 1))
    down_right = find_visible(x, y, rule=(1, 1))
    return [up_left, up, up_right, left, right, down_left, down, down_right]


def process(occupied_rule, limit_occupied_seats):
    global GRID, Y_LEN, X_LEN
    rounds = 0
    has_changed = True
    while has_changed:
        has_changed = False
        next_grid = [[g for g in GRID[i]] for i in range(Y_LEN)]
        for y in range(Y_LEN):
            for x in range(X_LEN):
                adjs = occupied_rule(x, y)
                num_occupied = len([adj for adj in adjs if adj == "#"])
                if GRID[y][x] == "L" and num_occupied == 0:
                    next_grid[y][x] = "#"
                    has_changed = True
                if GRID[y][x] == "#" and num_occupied >= limit_occupied_seats:
                    next_grid[y][x] = "L"
                    has_changed = True
        GRID = ["".join(g) for g in next_grid]
        rounds += 1 if has_changed else 0

    num_occupied_seats = sum([g.count("#") for g in GRID])
    return rounds, num_occupied_seats


rounds, num_occupied_seats = process(adjacents, 4)
print(f"P1. Num occupied seats after {rounds} rounds: {num_occupied_seats}")
GRID = read_grid()
rounds, num_occupied_seats = process(visible, 5)
print(f"P2. Num occupied seats after {rounds} rounds: {num_occupied_seats}")

from pathlib import Path


def check_tree_slope_x(line_of_trees, current_x, slope_x):
    current_x = current_x + slope_x
    current_x = current_x % len(line_of_trees)
    return line_of_trees[current_x] == "#", current_x


def check_trees(map, slope_x, slope_y):
    num_trees = 0
    current_x = 0
    current_y = slope_y
    while current_y < len(map):
        line_of_trees = map[current_y]
        is_tree, current_x = check_tree_slope_x(line_of_trees, current_x, slope_x)
        num_trees += int(is_tree)
        current_y += slope_y
    return num_trees


with open(Path(__file__).parent / "data" / "day03.txt", "r") as f:
    map = f.read().splitlines()

trees = check_trees(map, slope_x=3, slope_y=1)
print("First part")
print(f"Number of trees encountered: {trees}.")
print("======")
print("Second part")

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

multiply_trees = 1
for slope in slopes:
    slope_x, slope_y = slope
    print(f"Slope X: {slope_x}.\nSlope Y: {slope_y}.")
    slope_trees = check_trees(map, slope_x, slope_y)
    print(f"Num trees this slope: {slope_trees}.")
    multiply_trees *= slope_trees

print(f"Total multiplied trees: {multiply_trees}.")

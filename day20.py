import copy
import math
import numpy as np

with open("data/day20.txt") as f:
    lines = f.read().splitlines()

tiles = {}
tile_num = None
for line in lines:
    if line.startswith("Tile"):
        tile_num = int(line[5:9])
        tiles[tile_num] = {"grid": []}
        continue
    if line and tile_num:
        tiles[tile_num]["grid"].append(line)
    if not line:
        tile_num = None
all_bins = dict()


for t in tiles:
    tile = tiles[t]
    tile["up"] = tile["grid"][0]
    tile["right"] = "".join([t[-1] for t in tile["grid"]])
    tile["down"] = tile["grid"][-1]
    tile["left"] = "".join([t[0] for t in tile["grid"]])
    tile["bin_up"] = int(tile["up"].replace(".", "0").replace("#", "1"), 2)
    tile["bin_up_r"] = int(tile["up"][::-1].replace(".", "0").replace("#", "1"), 2)
    tile["bin_right"] = int(tile["right"].replace(".", "0").replace("#", "1"), 2)
    tile["bin_right_r"] = int(
        tile["right"][::-1].replace(".", "0").replace("#", "1"), 2
    )
    tile["bin_down"] = int(tile["down"].replace(".", "0").replace("#", "1"), 2)
    tile["bin_down_r"] = int(tile["down"][::-1].replace(".", "0").replace("#", "1"), 2)
    tile["bin_left"] = int(tile["left"].replace(".", "0").replace("#", "1"), 2)
    tile["bin_left_r"] = int(tile["left"][::-1].replace(".", "0").replace("#", "1"), 2)
    tile["bins"] = [
        tile["bin_up"],
        tile["bin_right"],
        tile["bin_down"],
        tile["bin_left"],
        tile["bin_up_r"],
        tile["bin_right_r"],
        tile["bin_down_r"],
        tile["bin_left_r"],
    ]
    tile["rots"] = [
        [
            tile["bin_up"],
            tile["bin_right"],
            tile["bin_down"],
            tile["bin_left"],
        ],  # rot 0
        [
            tile["bin_left_r"],  # up
            tile["bin_up"],  # right
            tile["bin_right_r"],  # down
            tile["bin_down"],  # left
        ],  # rot 1
        [
            tile["bin_down_r"],
            tile["bin_left_r"],
            tile["bin_up_r"],
            tile["bin_right_r"],
        ],  # rot 2
        [
            tile["bin_right"],
            tile["bin_down_r"],
            tile["bin_left"],
            tile["bin_up_r"],
        ],  # rot 3
    ]
    tile["flips"] = [
        [
            tile["bin_down"],
            tile["bin_right_r"],
            tile["bin_up"],
            tile["bin_left_r"],
        ],  # flip 0
        [
            tile["bin_right_r"],
            tile["bin_up_r"],
            tile["bin_left_r"],
            tile["bin_down_r"],
        ],  # flip 1
        [
            tile["bin_up_r"],
            tile["bin_left"],
            tile["bin_down_r"],
            tile["bin_right"],
        ],  # flip 2
        [
            tile["bin_left"],
            tile["bin_down"],
            tile["bin_right"],
            tile["bin_up"],
        ],  # flip 3
    ]
    tile["all_combs"] = tile["rots"] + tile["flips"]
    for bin in tile["bins"]:
        if bin in all_bins:
            all_bins[bin].append(t)
        else:
            all_bins[bin] = [t]

min_tiles = 1e5
for t in tiles:
    tile = tiles[t]
    tile["bins_n"] = []
    for b in tile["bins"]:
        tile["bins_n"].append(len(all_bins[b]))
    tile["num_bins"] = sum(tile["bins_n"])
    if tile["num_bins"] < min_tiles:
        min_tiles = tile["num_bins"]

corners = [t for t in tiles if tiles[t]["num_bins"] == min_tiles]
assert len(corners) == 4
ans = 1
for c in corners:
    ans *= c
print("P1:", ans)

TILE_LEN = len(tile["grid"][0])
SQUARE_SIZE = int(math.sqrt(len(tiles)))

for c in corners:
    tiles_pos = [[None] * SQUARE_SIZE for _ in range(SQUARE_SIZE)]
    tiles_edges = [[None] * SQUARE_SIZE for _ in range(SQUARE_SIZE)]
    tiles_combs = [[None] * SQUARE_SIZE for _ in range(SQUARE_SIZE)]
    tiles_pos[0][0] = c
    left_corner_comb = None
    for comb_i, comb in enumerate(tiles[c]["all_combs"]):
        if len(all_bins[comb[1]]) >= 2 and len(all_bins[comb[2]]) >= 2:
            left_corner_comb = comb_i
    assert left_corner_comb is not None
    tiles_edges[0][0] = tiles[c]["all_combs"][left_corner_comb]
    tiles_combs[0][0] = left_corner_comb

    used = {c}
    num_iters = 0
    while len(used) < len(tiles) and num_iters < (
        SQUARE_SIZE * SQUARE_SIZE * SQUARE_SIZE
    ):
        for row in range(SQUARE_SIZE):
            for column in range(SQUARE_SIZE):
                num_iters += 1
                if tiles_pos[row][column] is not None:
                    continue
                up = None
                left = None
                if (
                    column > 0
                    and row > 0
                    and tiles_pos[row - 1][column] is not None
                    and tiles_pos[row][column - 1] is not None
                ):
                    up = tiles_edges[row - 1][column][2]
                    left = tiles_edges[row][column - 1][1]
                elif column > 0 and row == 0 and tiles_pos[0][column - 1] is not None:
                    left = tiles_edges[row][column - 1][1]
                elif column == 0 and row > 0 and tiles_pos[row - 1][0] is not None:
                    up = tiles_edges[row - 1][0][2]
                possible_tiles = []
                for t in tiles:
                    if t in used:
                        continue
                    tile = tiles[t]
                    for comb_i, comb in enumerate(tile["all_combs"]):
                        check_up = comb[0] == up if up else True
                        check_left = comb[3] == left if left else True
                        if check_up and check_left:
                            possible_tiles.append(
                                {"t": t, "comb_i": comb_i, "comb": comb}
                            )

                if len(possible_tiles) == 1:
                    tiles_pos[row][column] = possible_tiles[0]["t"]
                    tiles_edges[row][column] = possible_tiles[0]["comb"]
                    tiles_combs[row][column] = possible_tiles[0]["comb_i"]
                    used.add(possible_tiles[0]["t"])
    if len(used) == len(tiles):
        print("Found combination!")
        break


def rotate(grid):
    new_grid = copy.deepcopy(grid)
    rotation = list(zip(*new_grid[::-1]))
    return np.array(rotation)


def flip(grid):
    new_grid = copy.deepcopy(grid)
    flipped = list(new_grid[::-1])
    return np.array(flipped)


def flip_rotate_comb(original_grid, comb_i):
    rotated = rotate(original_grid)
    if comb_i == 0:
        return original_grid
    if comb_i == 4:
        return flip(original_grid)
    elif comb_i == 1:
        return rotated
    elif comb_i == 5:
        return flip(rotated)
    elif comb_i == 2 or comb_i == 6:
        rotated_2 = rotate(rotated)
        if comb_i == 2:
            return rotated_2
        else:
            return flip(rotated_2)
    elif comb_i == 3 or comb_i == 7:
        rotated_3 = rotate(rotate(rotated))
        if comb_i == 3:
            return rotated_3
        else:
            return flip(rotated_3)
    else:
        assert False, "Unexpected value"


def get_comb_grid(t_num, comb_i):
    tile = tiles[t_num]
    if comb_i == 0 or comb_i == 4:
        arr_grid = np.empty((TILE_LEN, TILE_LEN), dtype=np.dtype(str))
        for grid_line_i, grid_line in enumerate(tile["grid"]):
            arr_grid[grid_line_i] = [t for t in grid_line]
        if comb_i == 0:
            return arr_grid
        else:
            return flip(arr_grid)
    return flip_rotate_comb(tile["grid"], comb_i)


IMG_LEN = SQUARE_SIZE * (TILE_LEN - 2)
image = np.empty((IMG_LEN, IMG_LEN), dtype=np.dtype(str))

for r in range(SQUARE_SIZE):
    for c in range(SQUARE_SIZE):
        comb_grid = get_comb_grid(tiles_pos[r][c], tiles_combs[r][c])
        assert type(comb_grid) == np.ndarray
        assert comb_grid.shape == (TILE_LEN, TILE_LEN)
        img_r_start = r * (TILE_LEN - 2)
        img_r_end = (r + 1) * (TILE_LEN - 2)
        imc_c_start = c * (TILE_LEN - 2)
        img_c_end = (c + 1) * (TILE_LEN - 2)
        image[img_r_start:img_r_end, imc_c_start:img_c_end] = comb_grid[1:-1, 1:-1]

MONSTER_PATTERN = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.splitlines()


def is_monster(img, start_r, start_c):
    for i in range(len(MONSTER_PATTERN)):
        for j in range(len(MONSTER_PATTERN[i])):
            if MONSTER_PATTERN[i][j] == "#" and img[start_r + i][start_c + j] != "#":
                return False
    return True


def count_hashtags_in_img(img):
    cnt = 0
    for i in range(IMG_LEN):
        for j in range(IMG_LEN):
            if str(img[i][j]) == "#":
                cnt += 1
    return cnt


hashtags_in_monster = sum([p.count("#") for p in MONSTER_PATTERN])

for rotate_comb in range(8):
    img_rotation = flip_rotate_comb(image, rotate_comb)
    monsters_count = 0
    for r in range(0, IMG_LEN - len(MONSTER_PATTERN)):
        for c in range(0, IMG_LEN - len(MONSTER_PATTERN[0])):
            if is_monster(img_rotation, r, c):
                monsters_count += 1
    if monsters_count > 0:
        print("Num monsters found:", monsters_count)
        count_hashtags = count_hashtags_in_img(img_rotation)
        water_roughness = count_hashtags - (hashtags_in_monster * (monsters_count))
        print("P2 (Water roughness):", water_roughness)
        break

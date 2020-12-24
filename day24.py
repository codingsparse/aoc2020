import re

dir_pat = re.compile(r"e|se|sw|w|nw|ne")

lines = open("data/day24.txt").read().splitlines()

black_tiles = set()
for line in lines:
    matches = dir_pat.findall(line)
    ew = 0
    ns = 0
    for m in matches:
        if m == "e":
            ew += 2
        elif m == "w":
            ew -= 2
        elif m == "se":
            ew += 1
            ns -= 3
        elif m == "nw":
            ew -= 1
            ns += 3
        elif m == "sw":
            ew -= 1
            ns -= 3
        elif m == "ne":
            ew += 1
            ns += 3
        else:
            assert False, "Unexpected value"
    if (ew, ns) in black_tiles:
        black_tiles.remove((ew, ns))
    else:
        black_tiles.add((ew, ns))
print("P1:", len(black_tiles))


days = 100
for d in range(1, days + 1):
    new_blacks = black_tiles.copy()
    possible_black_tiles = set()
    possible_white_tiles = set()
    for bt in black_tiles:
        possible_white_tiles.add(bt)
        for comb in [(2, 0), (-2, 0), (1, -3), (-1, 3), (-1, -3), (1, 3)]:
            possible_black_tile = (bt[0] + comb[0], bt[1] + comb[1])
            possible_black_tiles.add(possible_black_tile)

    for pb in possible_black_tiles:
        adjacent_blacks = set()
        for comb in [(2, 0), (-2, 0), (1, -3), (-1, 3), (-1, -3), (1, 3)]:
            adj = (pb[0] + comb[0], pb[1] + comb[1])
            if adj in black_tiles:
                adjacent_blacks.add(adj)
        if len(adjacent_blacks) == 2:
            new_blacks.add(pb)

    for pw in possible_white_tiles:
        adjacent_blacks = set()
        for comb in [(2, 0), (-2, 0), (1, -3), (-1, 3), (-1, -3), (1, 3)]:
            adj = (pw[0] + comb[0], pw[1] + comb[1])
            if adj in black_tiles:
                adjacent_blacks.add(adj)
        if len(adjacent_blacks) == 0 or len(adjacent_blacks) > 2:
            new_blacks.remove(pw)
    black_tiles = new_blacks
    # print(d, len(black_tiles))
print("P2:", len(black_tiles))

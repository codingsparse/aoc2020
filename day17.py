# test_state= [[[".#.",
# "..#",
# "###"]]]


def expand_state(state):
    new_state = [
        [
            [["."] * (len(state[0][0][0]) + 2) for _ in range(len(state[0][0]) + 2)]
            for _ in range(len(state[0]) + 2)
        ]
        for _ in range(len(state) + 2)
    ]
    for w in range(len(state)):
        for z in range(len(state[w])):
            for r in range(len(state[w][z])):
                for c in range(len(state[w][z][r])):
                    new_state[w + 1][z + 1][r + 1][c + 1] = state[w][z][r][c]
    return new_state


def neighbours(cw, cz, cr, cc, state, p2):
    neighbours = []
    for w in range(cw - 1, cw + 2) if p2 else [cw]:
        if p2 and (w < 0 or w >= len(state)):
            continue
        for z in range(cz - 1, cz + 2):
            if z < 0 or z >= len(state[w]):
                continue
            for r in range(cr - 1, cr + 2):
                if r < 0 or r >= len(state[w][z]):
                    continue
                for c in range(cc - 1, cc + 2):
                    if c < 0 or c >= len(state[w][z][r]):
                        continue
                    if w == cw and z == cz and r == cr and c == cc:
                        continue
                    neighbours.append(state[w][z][r][c])
    return neighbours


def compute(p2=False):
    state = [open("data/day17.txt").read().splitlines()]

    for gen in range(6):
        state = expand_state(state)
        next_state = [
            [
                [["."] * len(state[0][0][0]) for _ in range(len(state[0][0]))]
                for _ in range(len(state[0]))
            ]
            for _ in range(len(state))
        ]

        for w in range(len(state)):
            for z in range(len(state[w])):
                for r in range(len(state[w][z])):
                    for c in range(len(state[w][z][r])):
                        nighs = neighbours(w, z, r, c, state, p2)
                        num_active = len([n for n in nighs if n == "#"])
                        if state[w][z][r][c] == "#" and (
                            num_active == 2 or num_active == 3
                        ):
                            next_state[w][z][r][c] = "#"
                        if state[w][z][r][c] == "." and (num_active == 3):
                            next_state[w][z][r][c] = "#"
        state = next_state

    num_active = 0
    for w in range(len(state)):
        for z in range(len(state[w])):
            for r in range(len(state[w][z])):
                for c in range(len(state[w][z][r])):
                    if state[w][z][r][c] == "#":
                        num_active += 1
    return num_active


p1_num_active = compute()
print("P1:", p1_num_active)
p2_num_active = compute(p2=True)
print("P1:", p2_num_active)

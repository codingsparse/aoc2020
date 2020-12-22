import copy

p1 = []
p2 = []
current_p = None

for line in open("data/day22.txt").read().splitlines():
    if line.startswith("Player 1"):
        current_p = p1
        continue
    elif line.startswith("Player 2"):
        current_p = p2
        continue
    if line:
        current_p.append(int(line))


def play_game(p1, p2, is_part_2):
    p1_won = None

    seen = set()
    while p1 and p2:
        comb = str(p1) + str(p2)
        if is_part_2 and comb in seen:
            return p1, True
        seen.add(comb)

        p1_c = p1.pop(0)
        p2_c = p2.pop(0)

        if is_part_2 and len(p1) >= p1_c and len(p2) >= p2_c:
            new_p1 = [el for el in p1[:p1_c]]
            new_p2 = [el for el in p2[:p2_c]]
            _, p1_won = play_game(new_p1, new_p2, True)
        else:
            if p1_c > p2_c:
                p1_won = True
            elif p2_c > p1_c:
                p1_won = False

        if p1_won:
            p1.extend([p1_c, p2_c])
        else:
            p2.extend([p2_c, p1_c])

    if len(p1) > 0:
        p_won = p1
    else:
        p_won = p2
    return p_won, p1_won


for is_part_2 in [False, True]:
    part_p1 = copy.deepcopy(p1)
    part_p2 = copy.deepcopy(p2)
    p_won, _ = play_game(part_p1, part_p2, is_part_2)
    ans = 0
    len_p = len(p_won)
    for el, idx in zip(p_won, range(len_p, 0, -1)):
        ans += el * idx

    print(f'{"P1" if not is_part_2 else "P2"}:', ans)

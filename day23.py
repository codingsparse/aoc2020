input = "614752839"
cups = [int(x) for x in input]

n = len(cups)
i = 0
moves = 100
for m in range(moves):
    curr = cups[i]
    pick_idx = [(j + i) % n for j in [1, 2, 3]]
    pick = [cups[p] for p in pick_idx]
    next_curr = cups[(pick_idx[-1] + 1) % n]
    new_cups = [c for x, c in enumerate(cups) if x not in pick_idx]
    dest = (curr - 1) if curr > 1 else max(new_cups)
    while dest in pick:
        dest = (dest - 1) if dest > 1 else max(new_cups)
    dest_idx = (new_cups.index(dest) + 1) % n
    cups = new_cups[:dest_idx] + pick + new_cups[dest_idx:]
    i = cups.index(next_curr)

ans = ""
idx_1 = cups.index(1)
for i in range(1, n):
    idx = (idx_1 + i) % n
    ans += str(cups[idx])
print("P1", ans)

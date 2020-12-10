adapters = [int(l) for l in open("data/day10.txt").read().splitlines()]

adapters = sorted(adapters)

joltage = 0
differences = {1: 0, 2: 0, 3: 0}

for adapter in adapters:
    if (adapter - joltage) > 3:
        raise ValueError(
            "Adapter has voltage greater than 3 jolts from current joltage."
        )
    diff = adapter - joltage
    differences[diff] += 1
    joltage += diff
differences[3] += 1
joltage += 3
print(differences[1] * differences[3])

adapters = [0] + adapters

counts = {}


def ways_from(i):
    if joltage - adapters[i] <= 3:
        return 1
    if i in counts:
        return counts[i]
    count = 0
    for l in range(1, 4):
        next_el = i + l
        if next_el >= len(adapters):
            continue
        if adapters[next_el] - adapters[i] <= 3:
            count += ways_from(next_el)
    counts[i] = count
    return count


print(ways_from(0))

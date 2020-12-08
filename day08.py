lines = open("data/day08.txt").read().splitlines()

PART_1 = True
ACC = 0
LOOP = False
EXECUTED = [0] * len(lines)


def execute_line(i, lines):
    global ACC, LOOP
    if EXECUTED[i] > 0:
        if PART_1:
            print(f"LOOP! Value in ACC: {ACC}.")
        LOOP = True
        return None
    else:
        EXECUTED[i] += 1
    line = lines[i]
    inst, val = line.split()
    val = int(val)
    if inst == "nop":
        return i + 1
    if inst == "acc":
        ACC += val
        return i + 1
    if inst == "jmp":
        return i + val


# Part 1
i = 0
while not LOOP:
    i = execute_line(i, lines)

# Part 2
PART_1 = False
jmps = [j for j in range(len(lines)) if lines[j].startswith("jmp")]
nops = [j for j in range(len(lines)) if lines[j].startswith("nop")]
for jmp in jmps:
    jmp_line = lines[jmp]
    ex_lines = lines.copy()
    ex_lines[jmp] = jmp_line.replace("jmp", "nop")
    ACC = 0
    LOOP = False
    EXECUTED = [0] * len(lines)
    i = 0
    while not LOOP:
        i = execute_line(i, ex_lines)
        if i == len(ex_lines):
            print("Program terminates. ACC:", ACC)
            LOOP = True

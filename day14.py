import re

data = open("data/day14.txt").read()

mem_line_pat = re.compile(r"mem\[(\d+)\] = (\d+)")

mem = {}
mask_ones = 0
mask_zeros = 0
for line in data.splitlines():
    if line.startswith("mask"):
        mask_line = line.split("mask = ")[1]
        mask_ones = int("".join(["0" if m != "1" else "1" for m in mask_line]), 2)
        mask_zeros = int("".join(["1" if m == "0" else "0" for m in mask_line]), 2)
    if line.startswith("mem"):
        m = mem_line_pat.match(line)
        mem_address = int(m.group(1))
        mem_num = int(m.group(2))
        mem[mem_address] = (mem_num | mask_ones) & ~mask_zeros
print("P1:", sum(mem.values()))


mem = {}
mask_ones = 0
mask_floating_bits = []
for line in data.splitlines():
    if line.startswith("mask"):
        mask = line.split("mask = ")[1]

        mask_ones = int("".join(["1" if m == "1" else "0" for m in mask]), 2)
        mask_floating_bits = [i for i, e in enumerate(mask[::-1]) if e == "X"][::-1]
    if line.startswith("mem"):
        m = mem_line_pat.match(line)
        mem_address = int(m.group(1))
        mem_num = int(m.group(2))

        b = mem_address | mask_ones
        num_floating_bits = len(mask_floating_bits)
        for x in range(2 ** num_floating_bits):
            xbin = format(x, f"0{num_floating_bits}b")
            for bit, pos in zip(xbin, mask_floating_bits):
                if bit == "0":
                    b &= ~(1 << pos)
                elif bit == "1":
                    b |= 1 << pos
            mem[b] = mem_num
print("P2:", sum(mem.values()))

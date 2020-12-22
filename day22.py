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

p1_won = False
p2_won = False
while not p1_won and not p2_won:
    p1_c = p1.pop(0)
    p2_c = p2.pop(0)
    if p1_c > p2_c:
        p1.extend([p1_c, p2_c])
    elif p2_c > p1_c:
        p2.extend([p2_c, p1_c])
    else:
        assert False, "Unexpected value"
    p1_won = (len(p2) == 0)
    p2_won = (len(p1) == 0)

if p1_won:
    p_won = p1
else:
    p_won = p2

ans = 0
len_p = len(p_won)
for el, idx in zip(p_won,range(len_p,0,-1)):
    ans += (el * idx)
    
print('P1:', ans)
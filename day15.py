input = [8, 11, 0, 19, 1, 2]

# input = [3,1,2]

n = 0
last_spoken = dict()
last_last_spoken = dict()
for i, el in enumerate(input):
    last_spoken[el] = i
    n = el
i = len(input)
while i < 30000000:
    if i == 2020:
        print("P1:", n)
    last_last_n = last_last_spoken.get(n)
    if last_last_n is not None:
        n = last_spoken[n] - last_last_n
    else:
        n = 0

    if n in last_spoken:
        last_last_spoken[n] = last_spoken[n]

    last_spoken[n] = i
    i += 1

print("P2:", n)

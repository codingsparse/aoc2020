from functools import reduce

data = open("data/day13.txt").read().splitlines()
start_time = int(data[0])

ids = [int(e) for e in data[1].split(",") if e != "x"]

time = start_time
departure = False
while not departure:
    for id in ids:
        if time % id == 0:
            departure = True
            print("P1:", (time - start_time) * id)
            break
    time += 1

# taken from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


buses = data[1]
remainders = []
for i, el in enumerate(buses.split(",")):
    if el != "x":
        remainders.append(int(el) - i)

crt = chinese_remainder(ids, remainders)
print("P2:", crt)

P = 25

nums = []
num = 0
for n in open('data/day09.txt').read().splitlines():
    nums.append(int(n))

for i in range(P, len(nums)):
    preample = set(nums[i-P:i])
    num = nums[i]
    adds = []
    for x in preample:
        if (num - x) in preample:
            adds.append(x) 
    if sum(adds) == 0:
        print('P1:', num)
        break

finished = False
for i in range(2, len(nums)):
    cont = nums[i-2:i]
    s = sum(cont)
    while s < num and not finished:
        cont.append(nums[i])
        i += 1
        s = sum(cont)
        if s == num:
            print(min(cont), max(cont))
            print('P2:', min(cont) + max(cont))
            finished = True
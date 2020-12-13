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

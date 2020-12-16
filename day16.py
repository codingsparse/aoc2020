lines = open("data/day16.txt").read().splitlines()

your_ticket = None
nearby_tickets = None
ranges = {}
departure_fields = []
invalid_field_values = []
for i, line in enumerate(lines):
    if line.startswith("departure"):
        departure_fields.append(i)
    if " or " in line:
        ranges[i] = []
        l_ranges = line.split(": ")[1].split(" or ")
        for l_range in l_ranges:
            lp_range_x, lp_range_y = l_range.split("-")
            ranges[i].append(range(int(lp_range_x), int(lp_range_y) + 1))
    if "your ticket" in line:
        your_ticket = []
        continue
    if your_ticket is not None and len(your_ticket) == 0:
        your_ticket = [int(x) for x in line.split(",")]
    if "nearby tickets" in line:
        nearby_tickets = []
        continue
    if nearby_tickets is not None:
        fields = [int(e) for e in line.split(",")]
        valid_ticket = True
        for field in fields:
            valid = any(
                [field in range_in for range_ in ranges.values() for range_in in range_]
            )
            if not valid:
                invalid_field_values.append(field)
                valid_ticket = False
        if valid_ticket:
            nearby_tickets.append(fields)
print("P1:", sum(invalid_field_values))

possible_fields = {i: [True] * len(ranges) for i in ranges.keys()}
for ticket in nearby_tickets:
    for i, field in enumerate(ticket):
        for r in ranges:
            valid = any([field in range_in for range_in in ranges[r]])
            if not valid:
                possible_fields[r][i] = False

free_fields = [sum(possible_fields[i]) for i in possible_fields]
free_fields_idxs = [i[0] for i in sorted(enumerate(free_fields), key=lambda x: x[1])]

order_fields = [None] * len(possible_fields)
for i, idx in enumerate(free_fields_idxs):
    free_field = [i for i, x in enumerate(possible_fields[idx]) if x][0]
    order_fields[idx] = free_field
    for j in range(len(possible_fields)):
        possible_fields[j][free_field] = False

ans = 1
for departure_field in departure_fields:
    ans *= your_ticket[order_fields[departure_field]]
print("P2:", ans)

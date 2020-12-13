class Ship:
    direction = 0
    sn = 0
    ew = 0
    waypoint = (10, -1)

    def __init__(self):
        self.direction = 0
        self.sn = 0
        self.ew = 0
        self.waypoint = (10, -1)

    def move(self, inst):
        val = int(inst[1:])
        if inst.startswith("N"):
            self.sn -= val
        elif inst.startswith("S"):
            self.sn += val
        elif inst.startswith("W"):
            self.ew -= val
        elif inst.startswith("E"):
            self.ew += val

    def move_waypoint(self, inst):
        val = int(inst[1:])
        if inst.startswith("N"):
            self.waypoint = (self.waypoint[0], self.waypoint[1] - val)
        elif inst.startswith("S"):
            self.waypoint = (self.waypoint[0], self.waypoint[1] + val)
        elif inst.startswith("W"):
            self.waypoint = (self.waypoint[0] - val, self.waypoint[1])
        elif inst.startswith("E"):
            self.waypoint = (self.waypoint[0] + val, self.waypoint[1])

    def change_direction(self, inst):
        final_direction = self.direction
        value = int(inst[1:])
        if inst.startswith("L"):
            final_direction -= value
        elif inst.startswith("R"):
            final_direction += value
        self.direction = final_direction % 360

    def rotate_waypoint(self, inst):
        value = int(inst[1:])
        if inst.startswith("L"):
            value = 360 - value

        if value == 90:
            self.waypoint = (-self.waypoint[1], self.waypoint[0])
        elif value == 180:
            self.waypoint = (-self.waypoint[0], -self.waypoint[1])
        elif value == 270:
            self.waypoint = (self.waypoint[1], -self.waypoint[0])

    def follow(self, inst):
        value = int(inst[1:])
        if self.direction % 90 != 0:
            assert False, "Cannot follow direction if not precise!"
        dir = self.direction / 90
        if dir == 0:
            self.ew += value
        elif dir == 1 or dir == -3:
            self.sn += value
        elif dir == 2 or dir == -2:
            self.ew -= value
        elif dir == 3 or dir == -1:
            self.sn -= value

    def follow_waypoint(self, inst):
        value = int(inst[1:])
        self.sn += value * self.waypoint[1]
        self.ew += value * self.waypoint[0]

    def manhattan(self):
        return abs(self.sn) + abs(self.ew)

    def part1(self, inst):
        command = {
            "N": self.move,
            "S": self.move,
            "W": self.move,
            "E": self.move,
            "L": self.change_direction,
            "R": self.change_direction,
            "F": self.follow,
        }
        command[inst[0]](inst)

    def part2(self, inst):
        command = {
            "N": self.move_waypoint,
            "S": self.move_waypoint,
            "W": self.move_waypoint,
            "E": self.move_waypoint,
            "L": self.rotate_waypoint,
            "R": self.rotate_waypoint,
            "F": self.follow_waypoint,
        }
        command[inst[0]](inst)


insts = open("data/day12.txt").read().splitlines()
ship = Ship()
for inst in insts:
    ship.part1(inst)
print("P1:", ship.manhattan())
ship = Ship()
for inst in insts:
    ship.part2(inst)
print("P2:", ship.manhattan())

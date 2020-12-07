class Bag:
    name = ""
    contain = []
    is_contained_in = set()

    def __init__(self, name):
        self.name = name
        self.contain = []
        self.is_contained_in = set()


bags = {}

for line in open("data/day07.txt").read().splitlines():
    words = line.split()

    bag_name = " ".join(words[0:2])
    if bag_name in bags:
        b = bags[bag_name]
    else:
        b = Bag(bag_name)
        bags[bag_name] = b
    if words[4] == "no":
        continue
    for ix in range(4, len(words), 4):
        num = int(words[ix])
        in_bag = " ".join(words[ix + 1 : ix + 3])
        b.contain.extend([in_bag] * num)
        if in_bag in bags:
            bags[in_bag].is_contained_in.update({bag_name})
        else:
            new_bag = Bag(in_bag)
            new_bag.is_contained_in = {bag_name}
            bags[in_bag] = new_bag


def get_all_containing(bag):
    containing = {bag}
    if bag in bags:
        for b in bags[bag].is_contained_in:
            containing.update(get_all_containing(b))
    return containing


def num_bags_inside(bg):
    contains = 1
    if bg not in bags:
        return 1
    for b in bags[bg].contain:
        contains += num_bags_inside(b)
    return contains


print("Part 1:")
print(len(get_all_containing("shiny gold")) - 1)
print("Part 2:")
print(num_bags_inside("shiny gold") - 1)

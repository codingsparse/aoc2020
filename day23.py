input = "614752839"
CUPS = [int(x) for x in input]


def solve(is_part_2=False, debug=False):
    n = int(len(CUPS) + (1e6 - len(CUPS))) if is_part_2 else len(CUPS)

    class Node:
        def __init__(self, value):
            self.value = value
            self.next_node = None

    root_node = Node(CUPS[0])
    cupnodes_map = {CUPS[0]: root_node}
    prev_node = root_node
    for i in range(1, n):
        c = CUPS[i] if i < len(CUPS) else i + 1
        node = Node(c)
        prev_node.next_node = node
        cupnodes_map[c] = node
        prev_node = node
    prev_node.next_node = root_node
    curr_node = root_node
    moves = int(1e7) if is_part_2 else 100
    for m in range(moves):
        if debug and m % int(1e6) == 0:
            print(m)
        curr_value = curr_node.value
        pick_node = curr_node
        first_pick_node = pick_node.next_node
        pick_nodes_values = []
        for _ in range(3):
            pick_node = pick_node.next_node
            pick_nodes_values.append(pick_node.value)
        curr_node.next_node = pick_node.next_node
        dest_node_value = (curr_value - 1) if curr_value > 1 else n
        while dest_node_value in pick_nodes_values:
            dest_node_value = (dest_node_value - 1) if dest_node_value > 1 else n
        dest_node = cupnodes_map[dest_node_value]
        prev_dest_next = dest_node.next_node
        dest_node.next_node = first_pick_node
        pick_node.next_node = prev_dest_next
        curr_node = curr_node.next_node
    return cupnodes_map


cupnodes_p1 = solve()
start_node = cupnodes_p1[1]
ans_p1 = ""
for i in range(8):
    next_node = start_node.next_node
    ans_p1 += str(next_node.value)
    start_node = next_node
print("P1", ans_p1)

cupnodes_p2 = solve(is_part_2=True)
idx_1 = cupnodes_p2[1]
next_after_1 = idx_1.next_node
next_next_after_1 = next_after_1.next_node
print("P2", next_after_1.value * next_next_after_1.value)

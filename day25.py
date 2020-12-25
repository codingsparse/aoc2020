card_public_key = 7573546
door_public_key = 17786549
brute_force_iterations = 1e6


def solve(public_key=None, subject_number=7, fixed_size=None):
    val = 1
    num_loops = (
        range(1, int(brute_force_iterations)) if not fixed_size else range(fixed_size)
    )
    for loop_size in num_loops:
        val *= subject_number
        val = val % 20201227
        if val == public_key and not fixed_size:
            print("Found loop size:", loop_size)
            return loop_size
    if fixed_size:
        return val


card_loop_size = solve(card_public_key)
door_loop_size = solve(door_public_key)
if not card_loop_size and not door_loop_size:
    raise ValueError("Increase number of brute force iterations!")
if card_loop_size:
    loop_size = card_loop_size
    subject_number = door_public_key
else:
    loop_size = door_loop_size
    subject_number = card_public_key
encryption_key = solve(subject_number=subject_number, fixed_size=loop_size)
print("Encryption key:", encryption_key)

from pathlib import Path


def binary_partitioning(lowest_idx, highest_idx, split_type):
    assert split_type in ["F", "B", "L", "R"], "Invalid character for split."

    mid_idx = (lowest_idx + highest_idx) // 2
    if split_type == "F" or split_type == "L":
        return lowest_idx, mid_idx
    if split_type == "B" or split_type == "R":
        return mid_idx + 1, highest_idx


def partition(start_lowest_idx, start_highest_idx, splits):
    lowest_idx = start_lowest_idx
    highest_idx = start_highest_idx
    for split in splits:
        lowest_idx, highest_idx = binary_partitioning(lowest_idx, highest_idx, split)
    assert lowest_idx == highest_idx, "Split is not complete!"
    return lowest_idx


with open(Path(__file__).parent / "data" / "day05.txt", "r") as f:
    boarding_passes = f.read().splitlines()

# boarding_passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
seat_ids = []
for boarding_pass in boarding_passes:
    split_rows = boarding_pass[:-3]
    split_columns = boarding_pass[-3:]
    row = partition(0, 127, split_rows)
    column = partition(0, 7, split_columns)
    seat_id = row * 8 + column
    seat_ids.append(seat_id)
    print(f"{boarding_pass}: row {row}, column {column}, seat ID {seat_id}.")

print(f"Highest seat ID: {max(seat_ids)}")

min_seat_id = min(seat_ids)
max_seat_id = max(seat_ids)
for seat_id in range(min_seat_id, max_seat_id):
    is_present = seat_id in seat_ids
    if not is_present:
        print(f"Seat ID {seat_id} is not present!")

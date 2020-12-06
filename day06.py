from pathlib import Path


with open(Path(__file__).parent / "data" / "day06.txt", "r") as f:
    answered = set()
    counts = []
    for line in f.read().splitlines():
        if not line:
            counts.append(len(answered))
            answered = set()
            continue
        for c in line:
            answered.add(c)
    counts.append(len(answered))
    print(f"Sum of counts, questions anyone in each group answered: {sum(counts)}")


with open(Path(__file__).parent / "data" / "day06.txt", "r") as f:
    everyone_answered = None
    counts = []
    for line in f.read().splitlines():
        if not line:
            counts.append(len(everyone_answered))
            everyone_answered = None
            continue
        if everyone_answered is None:
            everyone_answered = set(line)
        else:
            everyone_answered = everyone_answered & set(line)
    counts.append(len(everyone_answered))
    print(f"Sum of counts, questions everyone in each group answered: {sum(counts)}")

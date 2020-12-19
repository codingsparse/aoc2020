import regex
from itertools import product

with open("data/day19.txt") as f:
    lines = f.read().splitlines()

RULES = {}
messages = None
for line in lines:
    if line == "":
        messages = []
        continue
    if messages is None:
        rule_num, rule = line.split(": ")
        if ("a" in rule) or ("b" in rule):
            RULES[rule_num] = {"letter": rule[1]}
        elif "|" in rule:
            first, second = rule.split(" | ")
            RULES[rule_num] = {"first": first.split(" "), "second": second.split(" ")}
        else:
            RULES[rule_num] = {"first": rule.split(" "), "second": None}

    if messages is not None and len(messages) >= 0:
        messages.append(line)

mem = {}


def expand_branch(r_num):
    if r_num in mem:
        return mem[r_num]
    branch = RULES[r_num]
    if branch.get("letter"):
        return [branch["letter"]]
    second_combinations = []
    if branch.get("second"):
        second_branch = [expand_branch(r) for r in branch["second"]]
        second_combinations = list(product(*second_branch))
    first_branch = [expand_branch(r) for r in branch["first"]]
    first_combinations = list(product(*first_branch))
    result = []
    for combination in first_combinations + second_combinations:
        result.append("".join(combination))
    mem[r_num] = result
    return result


root_rules = expand_branch("0")

rules_42 = expand_branch("42")
rules_31 = expand_branch("31")

rule_0 = regex.compile(
    r"(\L<rules_42>)+(\L<rules_31>)+", rules_42=rules_42, rules_31=rules_31
)

num_matches_p1 = 0
num_matches_p2 = 0
for message in messages:
    if message in root_rules:
        num_matches_p1 += 1

    if rule_match := rule_0.fullmatch(message):
        end_rule_42 = rule_match.regs[1][1]
        if end_rule_42 > len(message) - end_rule_42:
            num_matches_p2 += 1

print("P1:", num_matches_p1)
print("P2:", num_matches_p2)

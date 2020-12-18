def same_precedence(expression):
    r = ")"
    level = 0
    brackets_per_level = {0: 1}
    for c in expression[::-1]:
        if c.isdigit():
            r = c + r
        elif c.isspace():
            continue
        elif c in ["+", "*"]:
            r = ")" + c + r
            if level in brackets_per_level:
                brackets_per_level[level] += 1
            else:
                brackets_per_level[level] = 1
        elif c == "(":
            for _ in range(brackets_per_level[level] + 1):
                r = "(" + r
            brackets_per_level[level] = 0
            level -= 1
        elif c == ")":
            r = ")" + r
            level += 1
        else:
            assert False, "Unexpected value"
    for _ in range(brackets_per_level[0]):
        r = "(" + r
    return r


def different_precedence(expression):
    r = ")"
    for c in expression[::-1]:
        if c.isdigit():
            r = c + r
        elif c.isspace():
            continue
        elif c == "*":
            r = ")*(" + r
        elif c == "+":
            r = c + r
        elif c == "(":
            r = "((" + r
        elif c == ")":
            r = "))" + r
        else:
            assert False, "Unexpected value"
    r = "(" + r
    return r


results_p1 = []
results_p2 = []
expressions = open("data/day18.txt").read().splitlines()
for expression in expressions:
    exp_p1 = same_precedence(expression)
    exp_p2 = different_precedence(expression)
    results_p1.append(eval(exp_p1))
    results_p2.append(eval(exp_p2))
print("P1:", sum(results_p1))
print("P2:", sum(results_p2))

from collections import defaultdict

precedences = ["a op1 b op2 c op3 d",
    "(a op1 b) op2 c op3 d",
    "a op1 (b op2 c) op3 d",
    "a op1 b op2 (c op3 d)",
    "(a op1 b op2 c) op3 d",
    "a op1 (b op2 c op3 d)",
    "((a op1 b) op2 c) op3 d",
    "(a op1 b) op2 (c op3 d)",
    "(a op1 (b op2 c)) op3 d",
    "a op1 ((b op2 c) op3 d)",
    "a op1 (b op2 (c op3 d))"]

precedences_with_operations = []

for precedence in precedences:
    for op1 in ('+', '-', '/', '*'):
        for op2 in ('+', '-', '/', '*'):
            for op3 in ('+', '-', '/', '*'):
                replacing = precedence.replace('op1', op1)
                replacing = replacing.replace('op2', op2)
                replacing = replacing.replace('op3', op3)

                precedences_with_operations.append(replacing)
                
print(len(precedences_with_operations), precedences_with_operations[0:10])

offset = 0.00001

max_seen = 0
values = None

targets_per_numbers = defaultdict(lambda: set())

for a in range(0, 10):
    for b in range(0, 10):
        if a == b:
            continue
        for c in range(0, 10):
            if c == b or c == a:
                continue
            for d in range(0, 10):
                if d == c or d == b or d == a:
                    continue

                for precedence in precedences_with_operations:
                    try:
                        evaluated = eval(precedence, {"a": a, "b": b, "c": c, "d": d})
                        if int(evaluated) - offset < evaluated < int(evaluated) + offset:
                            targets_per_numbers["".join(sorted(str(a) + str(b) + str(c) + str(d)))].add(int(evaluated))

                    except ZeroDivisionError:
                        continue

for k, evaluated_collection in targets_per_numbers.items():
    verify = 1
    while verify in evaluated_collection:
        verify = verify + 1

    if (verify - 1 > max_seen):
        max_seen = verify - 1
        values = k

print(values, max_seen)
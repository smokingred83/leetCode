def calPoints(operations: [str]) -> int:
    scores = []
    actions = {
        "+": lambda: scores.append(int(scores[-1]) + int(scores[-2])),
        "D": lambda: scores.append(int(scores[-1]) * 2),
        "C": lambda: scores.pop()
    }
    for op in operations:
        if op in actions:
            actions[op]()
        else:
            scores.append(int(op))
    return sum(scores)


if __name__ == "__main__":
    res = calPoints(["5", "2", "C", "D", "+"])
    res

def judgeCircle(moves: str) -> bool:
    counts = {
        'U': 0,
        'D': 0,
        'L': 0,
        'R': 0
    }
    for m in moves:
        counts[m] += 1
    return counts['U'] == counts['D']\
        and counts['L'] == counts['R']


if __name__ == '__main__':
    res = judgeCircle('UD')
    res
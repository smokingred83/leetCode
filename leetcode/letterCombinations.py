_letters = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"],
    ["j", "k", "l"],
    ["m", "n", "o"],
    ["p", "q", "r", "s"],
    ["t", "u", "v"],
    ["w", "x", "y", "z"]
]

def letterCombinations(digits: str) -> [str]:
    if len(digits) == 1:
        return _letters[ord(digits[0]) - 50]
    result = []
    remaining = [_letters[ord(digits[i]) - 50] for i in range(len(digits))]
    combine(remaining, "", result)
    return result

def combine(remaining: [[str]], prefix: str, result: [str]):
    if len(remaining) == 1:
        for c in remaining[0]:
            result.append(prefix + c)
    else:
        for c in remaining[0]:
            combine(remaining[1:], prefix + c, result)


if __name__ == "__main__":
    res = letterCombinations("234")
    res
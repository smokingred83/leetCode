from typing import List

def generateParenthesis(n: int) -> List[str]:
    result = []
    generate("", n, n, result)
    return result

def generate(s, opening, closing, result):
    if opening == 0 and closing == 0:
        result.append(s)
    if opening > 0:
        generate(s + "(", opening - 1, closing, result)
    if closing > opening:
        generate(s + ")", opening, closing - 1, result)

if __name__ == "__main__":
    res = generateParenthesis(3)
    res
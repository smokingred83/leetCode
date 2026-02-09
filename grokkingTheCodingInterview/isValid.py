def isValid(s):
    cl2op = {")": "(", "]": "[", "}": "{"}
    stack = []
    for i in range(len(s)):
        if s[i] in cl2op and cl2op[s[i]] is stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    return len(stack) == 0

if __name__ == "__main__":
    res = isValid("{[()]]}")
    res
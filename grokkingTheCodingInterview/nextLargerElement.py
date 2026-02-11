def next_larger_element(arr):
    res = [-1] * len(arr)
    stack = []
    for i in range(len(arr) -1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res


def next_larger_element2(arr):
    res = [-1] * len(arr)
    stack = []
    for i in range(len(arr)):
        j = i -1
        while stack and arr[i] > stack[-1]:
            if arr[j] == stack[-1]:
                stack.pop()
            if res[j] == -1:
                res[j] = arr[i]
            j -= 1
        stack.append(arr[i])
    return res

if __name__ == "__main__":
    res = next_larger_element([3, 2, 5, 1, 4, 6])
    res
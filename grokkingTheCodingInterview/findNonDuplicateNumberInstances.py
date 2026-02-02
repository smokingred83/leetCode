def moveElements(arr):
    p1, p2, next_dupl = 0, 1, 1
    l = len(arr)
    while p2 < l:
        if arr[p1] >= arr[p2]:
            next_dupl = p1 + 1
            while p2 < l and arr[p1] >= arr[p2]:
                p2 += 1
            if p2 < l:
                arr[next_dupl], arr[p2] = arr[p2], arr[next_dupl]
        else:
            next_dupl += 1
            p2 += 1
        p1 += 1
    return next_dupl

def moveElements_proper_solution(arr: [int]) -> int:
    p1, p2 = 1, 0
    while p2 < len(arr):
        if arr[p1 - 1] != arr[p2]:
            arr[p1] = arr[p2]
            p1 += 1
        p2 += 1
    return p1

# Similar questions
# Problem 1
def remove(arr: [int], key: int):
    p1 = p2 = 0
    while p2 < len(arr):
        if arr[p2] != key:
            arr[p1] = arr[p2]
            p1 += 1
        p2 += 1
    return p1

if __name__ == "__main__":
    res = moveElements([2, 3, 3, 3, 6, 9, 9])
    res2 = moveElements_proper_solution([2, 3, 3, 3, 6, 9, 9])

    # Similar questions
    # Problem 1
    res = remove([3, 2, 3, 6, 3, 10, 9, 3], 3)
    res
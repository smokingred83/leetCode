def search(arr, target_sum):
    start = end = -1
    p1, p2 = 0, len(arr) -1
    while p1 < p2:
        tmp_sum = arr[p1] + arr[p2]
        if tmp_sum == target_sum:
            start, end = p1, p2
            break
        if tmp_sum < target_sum:
            p1 += 1
        else:
            p2 -= 1
    return [start, end]

if __name__ == "__main__":
    res = search([2, 5, 9, 11], 11)
    res
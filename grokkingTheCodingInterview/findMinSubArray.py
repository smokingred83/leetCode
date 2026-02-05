def findMinSubArray(arr: [int], s: int) -> int:
    start, accumulator = 0, 0
    _min = len(arr) + 1
    for end in range(len(arr)):
        accumulator += arr[end]
        while accumulator >= s:
            _min = min(_min, (end - start) + 1)
            accumulator -= arr[start]
            start += 1
    return _min if _min <= len(arr) else 0

if __name__ == "__main__":
    res = findMinSubArray([1, 1, 1], 10)
    res
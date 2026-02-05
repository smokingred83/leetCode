def find_averages(arr: [int], k: int) -> [int]:
    results = []
    start, _sum = 0, 0
    for end in range(len(arr)):
        _sum += arr[end]
        if (end - start) >= k - 1:
            results.append((_sum / k))
            _sum -= arr[start]
            start += 1
    return results

if __name__ == "__main__":
    res = find_averages([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    res
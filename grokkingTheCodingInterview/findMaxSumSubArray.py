def find_max_sum_sub_array(arr: [int], k: int):
    start, _sum, _max_sum = 0, 0, 0
    for end in range(len(arr)):
        _sum += arr[end]
        if (end - start) >= k - 1:
            _max_sum = max(_sum, _max_sum)
            _sum -= arr[start]
            start += 1
    return _max_sum

if __name__ == "__main__":
    res = find_max_sum_sub_array([2, 1, 5, 1, 3, 2], 3)
    res
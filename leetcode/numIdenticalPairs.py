def numIdenticalPairs(nums: [int]) -> int:
    num_freqs = {}
    for n in nums:
        num_freqs[n] = num_freqs.get(n, 0) + 1
    return sum([(v ** 2 - v) // 2 for v in num_freqs.values()])

if __name__ == "__main__":
    res = numIdenticalPairs([1,1,1,1])
    res
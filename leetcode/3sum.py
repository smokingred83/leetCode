def three_sum(nums: [int]) -> [[int]]:
    result = []
    remaining = nums
    while len(remaining) > 2:
        remaining = add_triplets(remaining[0], remaining[1:], result)
    return result

def add_triplets(target: int, nums: int, result: [int]) -> [int]:
    remaining, complements, triplets = [], set(), {}
    for n in nums:
        complement = -target - n
        if complement in complements:
            triplets[(target, complement, n)] = [target, complement, n]
        else:
            complements.add(n)
        if n != target:
            remaining.append(n)
    for t in triplets:
        result.append(triplets[t])
    return remaining

def three_sum2(nums: [int]) -> [[int]]:
    result = []
    for i in range(len(nums) - 2):
        visited = set(nums[:i])
        seen = set()
        if nums[i] not in visited:
            for j in range(i + 1, len(nums)):
                if nums[j] not in visited:
                    diff = -nums[i] - nums[j]
                    if diff in seen:
                        result.append([nums[i], nums[j], diff])
                        visited.add(nums[j])
                    else:
                        seen.add(nums[j])
    return result


if __name__ == "__main__":
    res = three_sum([0,0,0,0])
    res = three_sum([2, -4, 2, 2, 2, -4])
    res = three_sum([-1,0,1,2,-1,-4])
    res = three_sum([-1,0,1,0])
    res = three_sum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10])
    res
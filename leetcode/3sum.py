def three_sum(nums: [int]) -> [[int]]:
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
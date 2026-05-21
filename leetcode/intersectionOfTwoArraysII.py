from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    counter1, counter2, result = {}, {}, []

    for num in nums1:
        counter1[num] = counter1.get(num, 0) + 1
    for num in nums2:
        counter2[num] = counter2.get(num, 0) + 1

    for k, v in counter1.items():
        if k in counter2:
            result += [k for _ in range(min(counter1[k], counter2[k]))]

    return result

if __name__ == "__main__":
    res = intersect([4,9,5], [9,4,9,8,4])
    res
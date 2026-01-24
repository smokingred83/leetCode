def merge_sort_in_place(a: [int], left: int, right: int):
    if (right - left) > 1:
        middle = (left + right) // 2
        merge_sort_in_place(a, left, middle)
        merge_sort_in_place(a, middle, right)
        merge_in_place(a, left, middle, right)

def merge_in_place(a: [int], left: int, middle: int, right: int):
    l = [a[i] for i in range(left, middle)]
    r = [a[i] for i in range(middle, right)]
    i, j, c = 0, 0, left

    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            a[c] = r[j]
            j += 1
        elif l[i] <= r[j]:
            a[c] = l[i]
            i += 1
        c += 1

    while i < len(l):
        a[c] = l[i]
        i += 1
        c += 1
    while j < len(r):
        a[c] = r[j]
        j += 1
        c += 1


def merge_sort(nums: [int]) -> [int]:
    if len(nums) > 1:
        half = len(nums) // 2
        left = merge_sort(nums[:half])
        right = merge_sort(nums[half:])
        return merge(left, right)
    return nums


def merge(left, right) -> [int]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


if __name__ == '__main__':
    a = [7, 2, 5, 4, 1, 6, 0, 3]
    res = merge_sort_in_place(a, 0, len(a))
    res
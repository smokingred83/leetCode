from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result

def merge2(intervals: List[List[int]]) -> List[List[int]]:
    result = [intervals[0]]
    for right in range(1, len(intervals)):
        current = intervals[right]
        left = temp = 0
        while (left - temp) < len(result):
            if current[0] <= result[left - temp][1] and current[1] >= result[left - temp][0]:
                current[0] = min(current[0], result[left - temp][0])
                current[1] = max(current[1], result[left - temp][1])
                result.pop(left - temp)
                temp += 1
            left += 1
        result.append(current)
    return result

def merge1(intervals: List[List[int]]) -> List[List[int]]:
    sort(intervals, 0, len(intervals))
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])
    return result

def sort(intervals: List[List[int]], left: int, right: int):
    if (right - left) <= 1:
        return
    middle = (left + right) // 2
    sort(intervals, left, middle)
    sort(intervals, middle, right)
    sort_intervals(intervals, left, middle, right)

def sort_intervals(intervals: List[List[int]], l: int, m: int, r: int):
    left = [intervals[i] for i in range(l, m)]
    right = [intervals[i] for i in range(m, r)]
    c, i, j = l, 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            intervals[c] = left[i]
            i += 1
        else:
            intervals[c] = right[j]
            j += 1
        c += 1
    while i < len(left):
        intervals[c] = left[i]
        i += 1
        c += 1
    while j < len(right):
        intervals[c] = right[j]
        j += 1
        c += 1


if __name__ == "__main__":
    res = merge([[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]])
    res
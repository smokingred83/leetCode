def canMakeArithmeticProgression(arr: [int]) -> bool:
    max_num = max(arr)
    min_num = min(arr)
    diff = (max_num - min_num) / (len(arr) - 1)
    unordered = {num for num in arr}
    for i in range(len(arr)):
        if min_num + (diff * i) not in unordered:
            return False
    return True


if __name__ == '__main__':
    res = canMakeArithmeticProgression([1,2,3,2,5])
    res
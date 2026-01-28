def plusOne(digits: [int]) -> [int]:
    if digits[-1] == 9:
        if len(digits) == 1:
            return [1, 0]
        return plusOne(digits[:-1]) + [0]
    digits[-1] += 1
    return digits

if __name__ == '__main__':
    res = plusOne([9,9])
    res
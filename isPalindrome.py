def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reverse = 0
    pwr = 0
    temp = x
    map = dict()
    while temp > 0:
        map[pwr] = temp%10
        temp = temp // 10
        pwr += 1
    for i, num in map.items():
        reverse += num * 10**(pwr - 1 - i)
    return x == reverse

if __name__ == '__main__':
    res = isPalindrome(10)
    res
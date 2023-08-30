def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reverse = 0
    temp = x
    while temp > 0:
        reverse *= 10
        reverse += temp%10
        temp = temp // 10
    return x == reverse

if __name__ == '__main__':
    res = isPalindrome(10)
    res
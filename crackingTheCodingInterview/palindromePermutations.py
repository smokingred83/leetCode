def pal_perm(s: [str]) -> bool:
    checker = 0
    for c in s:
        chr = ord(c.lower()) - ord('a')
        if 0 <= chr < 26:
            checker ^= (1 << chr)
    # while checker > 1:
    #     if checker % 2 > 0:
    #         return False
    #     checker //= 2
    # return True
    # while checker > 1:
    #     if checker & 1:
    #         return False
    #     checker >> 1
    # return True
    return (checker & (checker - 1)) == 0

def pal_perm1(s: [str]) -> bool:
    char_freq = get_char_freq(s)
    single_char_count = 0
    for v in char_freq.values():
        if v % 2 == 1:
            single_char_count += 1
            if single_char_count > 1:
                return False
    return True


def get_char_freq(s):
    char_freq = {}
    for c in s:
        chr = ord(c.lower()) - ord('a')
        if 0 <= chr < 26:
            char_freq[c.lower()] = char_freq.get(c.lower(), 0) + 1
    return char_freq


if __name__ == "__main__":
    res = pal_perm("Tact Coat TT") #Tact Coat T
    res
def lengthOfLastWord(s: str) -> int:
    words = s.rstrip()
    c = 0
    for i in range(len(words)-1, -1, -1): #reversed(range(0, len(words))):
        if words[i] == ' ':
            break;
        c += 1;
    return c

if __name__ == '__main__':
    res = lengthOfLastWord("   fly me   to   the moon  ")
    res
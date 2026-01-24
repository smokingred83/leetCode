def checkIfPangram(sentence: str) -> bool:
    check = set()
    for c in sentence:
        chr = ord(c.lower()) - ord('a')
        if 0 <= chr < 26:
            check.add(c)
    return len(check) >= 26

if __name__ == "__main__":
    res = checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
    res
def mergeAlternately(word1: str, word2: str) -> str:
    len_w1 = len(word1)
    len_w2 = len(word2)
    merged = ""
    for i in range(0, min(len_w1, len_w2)):
        merged += word1[i] + word2[i]
    if len_w1 > len_w2:
        merged += word1[len_w2:]
    else:
        merged += word2[len_w1:]
    return merged

if __name__ == '__main__':
    mergeAlternately("ab", "pqrs")
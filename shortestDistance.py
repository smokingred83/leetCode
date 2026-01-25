def shortestDistance(words, word1, word2):
    pos1 = pos2 = -1
    min_dist = len(words)
    for i, word in enumerate(words):
        if word == word1:
            pos1 = i
        elif word == word2:
            pos2 = i
        if pos1 >= 0 and pos2 >= 0:
            dist = abs(pos1 - pos2)
            min_dist = min(min_dist, dist)
    return min_dist



if __name__ == "__main__":
    res = shortestDistance(
        ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"],
        "fox",
        "dog")
    res
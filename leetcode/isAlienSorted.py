class Solution:
    def isAlienSorted(self, words: [str], order: str) -> bool:
        al_dict = {c:i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)):
                if j >= len(w2) or al_dict[w2[j]] < al_dict[w1[j]]:
                    return False
                if al_dict[w1[j]] < al_dict[w2[j]]:
                    break
        return True

if __name__ == '__main__':
    s = Solution()
    res = s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    res
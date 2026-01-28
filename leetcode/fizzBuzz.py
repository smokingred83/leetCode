class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        result = []
        for i in range(1, n + 1):
            divisible_by_3 = i % 3 == 0
            divisible_by_5 = i % 5 == 0
            current = ""
            if divisible_by_3:
                current += "Fizz"
            if divisible_by_5:
                current += "Buzz"
            if current == "":
                current += str(i)
            result.append(current)
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.fizzBuzz(15)
    res
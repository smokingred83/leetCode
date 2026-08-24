from typing import List


def maxProfit(prices: List[int]) -> int:
    return sum(prices[i] - prices[i-1] if prices[i] > prices[i-1] else 0
               for i in range(1, len(prices)))


if __name__ == "__main__":
    res = maxProfit([7,1,5,3,6,4])
    res
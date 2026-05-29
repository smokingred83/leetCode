from typing import List

def max_recur(prices: List[int], idx: int) -> int:
    if idx >= len(prices):
        return 0

    best = 0
    for i in range(idx + 1, len(prices)):
        best = max(best,prices[i] - prices[idx])
    return max(best, max_recur(prices, idx + 1))

def maxProfit_recur(prices: List[int]) -> int:
    return max_recur(prices, 0)

def maxProfit(prices: List[int]) -> int:
    best, pre_min = 0, prices[0]
    for current in prices:
        tmp = current - pre_min
        best = best if best > tmp else tmp
        pre_min = pre_min if pre_min < current else current
    return best


if __name__ == "__main__":
    res = maxProfit([7,1,5,3,6,4])
    res
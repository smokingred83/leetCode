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
    profit, _min = 0, prices[0]
    if len(prices) > 1:
        for p in prices:
            _min = _min if _min < p else p
            tmp = p - _min
            profit = profit if profit > tmp else tmp
    return profit


if __name__ == "__main__":
    res = maxProfit([7,1,5,3,6,4])
    res
from typing import List


def coinsChange(coins: List[int], amount: int) -> int:
    memo = {}
    return coinsChange_memo(coins, amount, memo)

def coinsChange_memo(coins: List[int], amount: int, memo: dict):
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    if amount < 0:
        return -1

    results = []
    for coin in coins:
        result = coinsChange_memo(coins, amount - coin, memo)
        if result != -1:
            results.append(1 + result)
    memo[amount] = min(results) if results else -1
    return memo[amount]

def coinsChange_recur(coins: List[int], amount: int, idx: int, n: int) -> int:
    if amount < 0 or idx >= len(coins):
        return -1

    if amount == 0:
        return n

    change1 = -1
    if coins[idx] <= amount:
        change1 = coinsChange_recur(coins, amount - coins[idx], idx, n + 1)
    change2 = coinsChange_recur(coins, amount, idx + 1, n)

    if change1 == -1:
        return change2
    if change2 == -1:
        return change1
    return min(change1, change2)


if __name__ == "__main__":
    res = coinsChange([186,419,83,408], 6249)
    res
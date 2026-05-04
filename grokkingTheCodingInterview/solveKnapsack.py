def solveKnapsack_recur(profits: [int], weights: [int], capacity: int) -> int:
    return solve_recur(profits, weights, capacity, 0)

def solve_recur(profits: [int], weights: [int], capacity: int, idx: int) -> int:
    if idx >= len(profits) or capacity < 0:
        return 0
    new_capacity = capacity - weights[idx]
    profit1 = solve_recur(profits, weights, new_capacity, idx + 1)
    if new_capacity >= 0:
        profit1 += profits[idx]
    profit2 = solve_recur(profits, weights, capacity, idx + 1)
    return max(profit1, profit2)

def solveKnapsack_memo(profits: [int], weights: [int], capacity: int) -> int:
    if len(profits) <= 0:
        return 0
    memo = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    solve_memo(profits, weights, capacity, len(profits)-1, memo)
    return memo[len(profits) - 1][capacity]

def solve_memo(profits: [int], weights: [int], capacity: int, idx: int, memo: [[int]]) -> int:
    if idx < 0 or capacity < 0:
        return 0

    if memo[idx][capacity] > -1:
        return memo[idx][capacity]

    new_capacity = capacity - weights[idx]
    profit1 = solve_memo(profits, weights, new_capacity, idx - 1, memo)
    if new_capacity >= 0:
        profit1 += profits[idx]
    profit2 = solve_memo(profits, weights, capacity, idx - 1, memo)

    memo[idx][capacity] = max(profit1, profit2)
    return memo[idx][capacity]

def solveKnapsack_tab(profits: [int], weights: [int], capacity: int) -> int:
    dp = [[0 for x in range(capacity+1)] for y in range(len(profits)+1)]
    for idx in range(1, len(profits)+1):
        for cap in range(capacity+1):
            weight = weights[idx-1]
            if weight <= cap:
                profit = profits[idx-1]
                dp[idx][cap] = max(profit + dp[idx-1][cap-weight], dp[idx-1][cap])
            else:
                dp[idx][cap] = dp[idx-1][cap]
    print_selected_elements(dp, weights, capacity)
    return dp[len(profits)][capacity]

def solveKnapsack_const_space(profits: [int], weights: [int], capacity: int) -> int:
    if len(profits) <= 0:
        return 0
    dp = [[0 for x in range(capacity+1)] for y in range(2)]
    for cap in range(1, capacity+1):
        if weights[0] <= cap:
            dp[0][cap] = dp[1][cap] = profits[0]

    for i in range(1, len(weights)):
        for cap in range(1, capacity+1):
            profit1 = 0
            if weights[i] <= cap:
                profit1 = profits[i] + dp[(i-1)%2][cap-weights[i]]
            profit2 = dp[(i-1)%2][cap]
            dp[i%2][cap] = max(profit1, profit2)
    return dp[(len(weights)-1)%2][capacity]

def solveKnapsack_one_array(profits: [int], weights: [int], capacity: int) -> int:
    if len(profits) <= 0:
        return 0

    dp = [0 for x in range(capacity+1)]
    for cap in range(1, capacity + 1):
        if weights[0] <= cap:
            dp[cap] = profits[0]

    for i in range(1, len(weights)):
        for cap in range(capacity, 0, -1):
            profit1 = 0
            if weights[i] <= cap:
                profit1 = profits[i] + dp[cap-weights[i]]
            profit2 = dp[cap]
            dp[cap] = max(profit1, profit2)
    return dp[capacity]

def print_selected_elements(dp: [[int]], weights: [int], capacity):
    idx, cap = len(weights), capacity
    while cap > 0:
        if dp[idx][cap] == dp[idx - 1][cap]:
            idx -= 1
        else:
            print(f'Item {idx - 1}')
            cap -= weights[idx - 1]

if __name__ == "__main__":
    res = solveKnapsack_one_array([4, 5, 3, 7], [2, 3, 1, 4], 5)
    res
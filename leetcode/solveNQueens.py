from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    grid = [[0 for _ in range(n)] for _ in range(n + 1)]
    solve(n - 1, [i for i in range(n)], grid, result)
    return result

def solve(row, columns, grid, result):
    if row < 0:
        board = ["".join("Q" if j == 1 else "." for j in grid[i]) for i in range(len(grid) - 1)]
        result.append(board)
    for i, col in enumerate(columns):
        if check_if_valid(grid, row, col):
            grid[row][col] = 1
            solve(row - 1, columns[0:i] + columns[i + 1:], grid, result)
            grid[row][col] = 0


def check_if_valid(grid, row, col):
    r = row + 1
    left = col - 1
    right = col + 1
    while r < len(grid):
        if left >= 0 and grid[r][left] == 1:
            return False
        if right < len(grid[r]) and grid[r][right] == 1:
            return False
        r += 1
        left -= 1
        right += 1
    return True


if __name__ == "__main__":
    res = solveNQueens(4)
    res
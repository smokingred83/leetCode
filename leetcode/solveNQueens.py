from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    grid = [["." for _ in range(n)] for _ in range(n + 1)]
    solve(n - 1, [i for i in range(n)], [], grid, result)
    return result

def solve(row, columns, diags, grid, result):
    if row < 0:
        board = ["".join(grid[i]) for i in range(len(grid) - 1)]
        result.append(board)
        return
    for i, c in enumerate(columns):
        if c not in diags:
            grid[row][c] = "Q"
            update = [diags[i] - 1 if i % 2 == 0 else diags[i] + 1 for i in range(len(diags))]
            solve(row - 1, columns[0:i] + columns[i + 1:], update + [c-1, c+1], grid, result)
            grid[row][c] = "."


def solve1(row, columns, grid, result):
    if row < 0:
        board = ["".join("Q" if j == 1 else "." for j in grid[i]) for i in range(len(grid) - 1)]
        result.append(board)
    for i, col in enumerate(columns):
        if check_if_valid(grid, row, col):
            grid[row][col] = "Q"
            solve(row - 1, columns[0:i] + columns[i + 1:], grid, result)
            grid[row][col] = "."

def check_if_valid(grid, row, col):
    r = row + 1
    left = col - 1
    right = col + 1
    while r < len(grid):
        if left >= 0 and grid[r][left] == "Q":
            return False
        if right < len(grid[r]) and grid[r][right] == "Q":
            return False
        r += 1
        left -= 1
        right += 1
    return True


if __name__ == "__main__":
    res = solveNQueens(4)
    res
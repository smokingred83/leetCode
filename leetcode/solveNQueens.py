from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    solve(n - 1, [-1 for _ in range(n)], result)
    return result

def solve(row, columns, result):
    if row < 0:
        board = ["".join(["Q" if i == v else "." for i in range(len(columns))]) for _, v in enumerate(columns)]
        result.append(board)
        return
    for col in range(len(columns)):
        if check_if_valid(columns, row, col):
            columns[col] = row
            solve(row - 1, columns, result)
            columns[col] = -1

def check_if_valid(columns, row1, col1) -> bool:
    for row2 in range(len(columns) - 1, row1, -1):
        col2 = columns.index(row2)
        if col1 == col2:
            return False
        diff_row = abs(row2 - row1)
        diff_col = abs(col2 - col1)
        if diff_row == diff_col:
            return False
    return True

def solveNQueens1(n: int) -> List[List[str]]:
    result = []
    grid = [["." for _ in range(n)] for _ in range(n + 1)]
    solve(n - 1, [i for i in range(n)], [], grid, result)
    return result

def solve1(row, columns, diags, grid, result):
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

def solve1_1(row, columns, grid, result):
    if row < 0:
        board = ["".join("Q" if j == 1 else "." for j in grid[i]) for i in range(len(grid) - 1)]
        result.append(board)
    for i, col in enumerate(columns):
        if check_if_valid(grid, row, col):
            grid[row][col] = "Q"
            solve(row - 1, columns[0:i] + columns[i + 1:], grid, result)
            grid[row][col] = "."

def check_if_valid1(grid, row, col):
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
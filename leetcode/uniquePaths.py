def uniquePaths(m: int, n: int) -> int:
    grid = [[0] * n for _ in range(m)]
    return count_paths(grid, 0, 0)

def count_paths(grid: [[int]], m: int, n: int) -> int:
    if m == len(grid) -1 and n == len(grid[-1]) -1:
        return 1
    if m >= len(grid) or n >= len(grid[-1]):
        return 0
    if grid[m][n] == 0:
        grid[m][n] = count_paths(grid, m + 1, n) + count_paths(grid, m, n + 1)
    return grid[m][n]

if __name__ == "__main__":
    res = uniquePaths(3, 2)
    res
def spiralOrder(matrix: [[int]]) -> [int]:
    rows = len(matrix)
    if rows <= 0 or len(matrix[0]) <= 0:
        return []
    columns = len(matrix[0])
    spiral = matrix[0][:]
    if rows > 1:
        spiral += [matrix[i][-1] for i in range(1, rows)]
        if columns > 1:
            spiral += [matrix[-1][i] for i in range(columns-2, -1, -1)]
            spiral += [matrix[i][0] for i in range(rows-2, 0, -1)]
    return spiral + spiralOrder([a[1:-1] for a in matrix[1:-1]])


if __name__ == '__main__':
    res = spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
    res
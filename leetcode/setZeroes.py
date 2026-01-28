def setZeroes(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zeros = {}
    for row, _ in enumerate(matrix):
        for col, n in enumerate(matrix[row]):
            if n == 0:
                if row in zeros.keys():
                    zeros[row].add(col)
                else:
                    zeros[row] = {col}
    row_len = len(matrix[0])
    for row, columns in zeros.items():
        matrix[row] = [0]*row_len
        for column in columns:
            for row in matrix:
                row[column] = 0

if __name__ == '__main__':
    setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
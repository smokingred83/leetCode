def diagonalSum(mat: [[int]]) -> int:
    l = len(mat)
    diag = sum([mat[i][i] + mat[i][l-1-i] for i in range(l)])
    if l % 2 != 0:
        diag -= mat[l//2][l//2]
    return diag


if __name__ == '__main__':
    res = diagonalSum([[1,2,3],[4,5,6],[7,8,9]])
    res
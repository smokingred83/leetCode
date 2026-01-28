def tictactoe(moves: [[int]]) -> str:
    winnings = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[0, 2], [1, 1], [2, 0]]
    ]
    a = []
    b = []
    for i, move in enumerate(moves):
        if i % 2 == 0:
            a.append(move)
        else:
            b.append(move)
    for winning in winnings:
        if all([w in a for w in winning]):
            return 'A'
        if all([w in b for w in winning]):
            return 'B'
    return "Draw" if len(moves) == 9 else "Pending"

if __name__ == '__main__':
    res = tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]])
    res
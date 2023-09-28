def isRobotBounded(instructions: str) -> bool:
    turns = {
        'N': {
            'R': 'E',
            'L': 'W'
        },
        'S': {
            'R': 'W',
            'L': 'E'
        },
        'E': {
            'R': 'S',
            'L': 'N'
        },
        'W': {
            'R': 'N',
            'L': 'S'
        }
    }
    moves = {
        'N': lambda pos: [sum(x) for x in zip(pos, [1, 0])],
        'S': lambda pos: [sum(x) for x in zip(pos, [-1, 0])],
        'E': lambda pos: [sum(x) for x in zip(pos, [0, 1])],
        'W': lambda pos: [sum(x) for x in zip(pos, [0, -1])],
    }
    direction = 'N'
    position = [0, 0]
    for i in range(len(instructions)):
        ins = instructions[i]
        if ins == 'G':
            position = moves[direction](position)
        else:
            direction = turns[direction][ins]
    return position == [0, 0] or direction != 'N'


if __name__ == '__main__':
    res = isRobotBounded('LLGRL')
    res
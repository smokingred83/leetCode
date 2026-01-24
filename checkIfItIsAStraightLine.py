from typing import List


def checkStraightLine(coordinates: List[List[int]]) -> bool:
    xs, ys = zip(*coordinates)
    if len(set(xs)) == 1 or len(set(ys)) == 1:
        return True
    ratios = set()
    for x, y in coordinates[1:]:
        rise = y - coordinates[0][1]
        run = x - coordinates[0][0]
        if run == 0:
            return False
        ratios.add(rise / run)
        if len(ratios) > 1:
            return False
    return True


# Straight line equation:
# y − y1 = m(x − x1)
# https://leetcode.com/problems/check-if-it-is-a-straight-line/solutions/5135990/python3-check-if-it-is-a-straight-line
# y - y0 = (dy / dx) * (x - x0)
def checkStraightLine2(coordinates: List[List[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dx, dy = x1 - x0, y1 - y0
    return all(dx * (y - y0) == dy * (x - x0) for x, y in coordinates[1:])


if __name__ == '__main__':
    res = checkStraightLine([[2, 1], [4, 2], [6, 3]])
    res

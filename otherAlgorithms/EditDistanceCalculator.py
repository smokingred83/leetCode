class EditDistanceCalculator:
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
        self.grid = list()
        # self.grid = [
        #    [max(i, j) if min(i, j) == 0 else 0
        #     for j in range(len(text2) + 1)]
        #    for i in range(len(text1) + 1)]

    def get_distance(self):
        self.grid.append([i for i in range(len(self.text2) + 1)])
        for i in range(len(self.text1)):
            self.grid.append([i + 1] + ([0] * len(self.text2)))

        for i in range(1, len(self.grid)):
            for j in range(1, len(self.grid[0])):
                self.grid[i][j] = self.calculate(i, j)
        return self.grid[-1][-1]

    def calculate(self, i, j):
        replace = self.grid[i - 1][j - 1]
        if self.text1[i - 1] is self.text2[j - 1]:
            return replace
        replace += 1
        delete = self.grid[i - 1][j] + 1
        insert = self.grid[i][j - 1] + 1
        return min(replace, delete, insert)

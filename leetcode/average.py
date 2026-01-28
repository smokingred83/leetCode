def average(salary: [int]) -> float:
    result = max_s = min_s = salary[0]
    for i in range(1, len(salary), 1):
        max_s = max(max_s, salary[i])
        min_s = min(min_s, salary[i])
        result += salary[i]
    return (result - max_s - min_s) / (len(salary) - 2)


if __name__ == '__main__':
    res = average([4000, 3000, 1000, 2000])
    res

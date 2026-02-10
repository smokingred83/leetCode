def move_disks(n: int, origin: [int], buffer: [int], dest: [int]):
    if n <= 0:
        return
    move_disks(n - 1, origin, dest, buffer)
    dest.append(origin.pop())
    move_disks(n - 1, buffer, origin, dest)

if __name__ == "__main__":
    origin = [n for n in range(21, 0, -1)]
    dest = []
    move_disks(4, origin, [], dest)
    print(dest)
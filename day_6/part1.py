with open("/home/manu/Desktop/AdventOfCode2024/day_6/input.txt") as f:
    grid = f.read().splitlines()

rows, cols = len(grid), len(grid[0])
pgx, pgy = None, None
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]
current_dir = 0

for y in range(rows):
    if '^' in grid[y]:
        pgx = grid[y].index('^')
        pgy = y
        break

res = []

while 0 <= pgx < rows-1 and 0 <= pgy < cols-1:
    if current_dir == 0:
        if grid[pgy - 1][pgx] == "#":
            current_dir = 1
        else:
            pgy += directions[current_dir][1]
            res.append((pgx, pgy))
    elif current_dir == 1:
        if grid[pgy][pgx + 1] == "#":
            current_dir = 2
        else:
            pgx += directions[current_dir][0]
            res.append((pgx, pgy))
    elif current_dir == 2:
        if grid[pgy + 1][pgx] == "#":
            current_dir = 3
        else:
            pgy += directions[current_dir][1]
            res.append((pgx, pgy))
    elif current_dir == 3:
        if grid[pgy][pgx - 1] == "#":
            current_dir = 0
        else:
            pgx += directions[current_dir][0]
            res.append((pgx, pgy))

res = list(set(res))
print(len(res))
with open("C:/Users/manue/Desktop/AdventOfCode2024/day_6/input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]

rows, cols = len(grid), len(grid[0])
pgx, pgy = None, None
directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

for y in range(rows):
    if '^' in grid[y]:
        pgx = grid[y].index('^')
        pgy = y
        break

def loops(grid, x, y):
    visited = []
    current_dir = 0

    while True:
        visited.append((x, y, current_dir))
        if not (0 <= x < rows-1 and 0 <= y < cols-1):
            return False
        
        if current_dir == 0:
            if grid[y - 1][x] == "#":
                current_dir = 1
            else:
                y += directions[current_dir][1]
        elif current_dir == 1:
            if grid[y][x + 1] == "#":
                current_dir = 2
            else:
                x += directions[current_dir][0]
        elif current_dir == 2:
            if grid[y + 1][x] == "#":
                current_dir = 3
            else:
                y += directions[current_dir][1]
        elif current_dir == 3:
            if grid[y][x - 1] == "#":
                current_dir = 0
            else:
                x += directions[current_dir][0]
        
        if (x, y, current_dir) in visited:
            return True

res = 0
for r in range(rows):
    for c in range(cols):
        if grid[r][c] != ".":
            continue
        grid[r][c] = "#"
        if loops(grid, pgx, pgy):
            res += 1
        grid[r][c] = "."

print(res)
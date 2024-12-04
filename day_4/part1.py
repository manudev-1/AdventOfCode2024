def count_xmas_in_grid(grid):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1) 
    ]
    target = "XMAS"
    count = 0
    rows, cols = len(grid), len(grid[0])

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def find_word(x, y, dx, dy):
        for i, char in enumerate(target):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != char:
                return False
        return True

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "X":
                for dx, dy in directions:
                    if find_word(r, c, dx, dy):
                        count += 1

    return count

with open("/home/manu/Desktop/AdventOfCode2024/day_4/input.txt") as f:
    grid = f.read().splitlines()

result = count_xmas_in_grid(grid)
print(result)

def count_xmas_in_x_shape(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_x_mas(x, y):
        positions = [
            (x-1, y-1), (x+1, y+1),  # Top-left to bottom-right
            (x-1, y+1), (x+1, y-1)   # Top-right to bottom-left
        ]
    
        if all(is_valid(nx, ny) for nx, ny in positions[:2]):
            diag1 = grid[x-1][y-1] + grid[x][y] + grid[x+1][y+1]
            if diag1 == "MAS" or diag1 == "SAM":
                if all(is_valid(nx, ny) for nx, ny in positions[2:]):
                    diag2 = grid[x-1][y+1] + grid[x][y] + grid[x+1][y-1]
                    if diag2 == "MAS" or diag2 == "SAM":
                        return True
        return False

    for r in range(1, rows-1):
        for c in range(1, cols-1):
            if grid[r][c] == "A":
                if check_x_mas(r, c):
                    count += 1

    return count

with open("/home/manu/Desktop/AdventOfCode2024/day_4/input.txt") as f:
    grid = f.read().splitlines()

result = count_xmas_in_x_shape(grid)
print(result)

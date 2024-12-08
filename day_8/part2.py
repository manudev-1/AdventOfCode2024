with open("C:/Users/manue/Desktop/AdventOfCode2024/day_8/input.txt") as f:
    lines = [ line.strip() for line in f]

rows = len(lines)
cols = len(lines[0])

antennas = {}

for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char != ".":
            if char not in antennas: antennas[char] = []
            antennas[char].append((r,c))

antinodes = set()

for array in antennas.values():
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j: continue
            r1, c1 = array[i]
            r2, c2 = array[j]
            dr = r2 - r1
            dc = c2 - c1
            r = r1
            c = c1
            while 0 <= r < rows and 0 <= c < cols:
                antinodes.add((r, c))
                r += dr
                c += dc


print(len(antinodes))
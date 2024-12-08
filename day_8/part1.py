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
        for j in range(i+1, len(array)):
            r1, c1 = array[i]
            r2, c2 = array[j]
            antinodes.add((2*r1 - r2, 2*c1 - c2))
            antinodes.add((2*r2 - r1, 2*c2 - c1))


print(len([0 for r, c in antinodes if 0 <= r < rows and 0 <= c < cols]))
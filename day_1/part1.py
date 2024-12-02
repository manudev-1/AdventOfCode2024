with open("/home/manu/Desktop/AdventOfCode2024/day_1/input.txt") as f:
    lines = f.read().splitlines()

left = []
right = []

for line in lines:
    x, y = line.split()
    left.append(int(x))
    right.append(int(y))

left = sorted(left)
right = sorted(right)

res = []
for x, y in zip(left, right):
    res.append(abs(x - y))

print(sum(res))
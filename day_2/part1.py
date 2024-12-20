with open("/home/manu/Desktop/AdventOfCode2024/day_2/input.txt") as f:
    lines = f.read().splitlines()

k = 0

for line in lines:
    splitted = line.split(" ")
    levels = [int(x) for x in splitted] 

    is_increasing = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))

    if is_increasing or is_decreasing:
        differences = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]
        
        if all(1 <= diff <= 3 for diff in differences):
            k += 1

print(k)

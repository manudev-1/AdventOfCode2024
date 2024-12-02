with open("/home/manu/Desktop/AdventOfCode2024/day_2/input.txt") as f:
    lines = f.read().splitlines()

k = 0

def is_safe(levels):
    is_increasing = all(levels[i] <= levels[i + 1] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i] >= levels[i + 1] for i in range(len(levels) - 1))

    if is_increasing or is_decreasing:
        differences = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]
        return all(1 <= diff <= 3 for diff in differences)
    return False


for line in lines:
    splitted = line.split(" ")
    levels = [int(x) for x in splitted] 

    if is_safe(levels):
        k += 1
        continue

    for i in range(len(levels)):
        modified_lvls = levels[:i] + levels[i+1:]
        if is_safe(modified_lvls):
            k += 1
            break

print(k)
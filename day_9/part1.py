with open("/home/manu/Desktop/AdventOfCode2024/day_9/input.txt") as f:
    line = f.read()

output = []
c = 0
for index, char in enumerate(line):
    if index % 2 == 0:
        output += [c] * int(char)
        c += 1
    else:
        output += [-1] * int(char)

free_space = [i for i, char in enumerate(output) if char == -1]

for i in free_space:
    while output[-1] == -1: output.pop()
    if i >= len(output): break
    output[i] = output.pop()

res = sum(i * char for i, char in enumerate(output))

print(res)
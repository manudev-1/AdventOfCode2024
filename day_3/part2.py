import re

with open("/home/manu/Desktop/AdventOfCode2024/day_3/input.txt") as f:
    lines = f.read().splitlines()

line = lines[0]

first_parts = line.split("mul(")
regexp = re.compile(r"\d+,\d+")

DO = True

res = 0
for part in first_parts:
    print(part)
    
    sub_parts = part.split(")")

    if any(regexp.match(part) for part in sub_parts):
        number = sub_parts[0]
        try:
            if DO:
                res += int(number.split(",")[0]) * int(number.split(",")[1])
        except Exception as e:
            continue

    if 'do()' in part:
        DO = True
    elif 'don\'t()' in part:
        DO = False

print(res)
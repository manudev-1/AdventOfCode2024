def is_correct_order(update, rules):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            first_page = update[i]
            second_page = update[j]
            if second_page in rules.get(first_page, []):
                continue
            else:
                return False
    return True
    
with open("C:/Users/manue/Desktop/AdventOfCode2024/day_5/rules.txt") as f:
    rules = f.read().splitlines()
    
rules_dict = {}

for line in rules:
    first, second = line.split("|")
    if not first in rules_dict:
        rules_dict[first] = [second]
    else: 
        rules_dict[first].append(second)
    
with open("C:/Users/manue/Desktop/AdventOfCode2024/day_5/updates.txt") as f:
    updates = f.read().splitlines()

update_arr = [update.split(",") for update in updates]

res = 0
for update in update_arr:
    if is_correct_order(update, rules_dict):
        middle_page = update[len(update) // 2]
        res += int(middle_page)
    
print(res)
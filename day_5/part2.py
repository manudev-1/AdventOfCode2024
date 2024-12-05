from collections import deque, defaultdict

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

def topological_sort(pages, rules):
    relevant_rules = {page: [dep for dep in deps if dep in pages] for page, deps in rules.items() if page in pages}
    all_pages = set(pages)
    in_degree = {page: 0 for page in all_pages}
    
    for page in relevant_rules:
        for dep in relevant_rules[page]:
            in_degree[dep] += 1

    queue = deque([page for page in all_pages if in_degree[page] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        
        for dep in relevant_rules.get(current, []):
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)
    
    if len(sorted_pages) == len(all_pages):
        return [page for page in sorted_pages if page in pages]
    else:
        return []
    
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
    if not is_correct_order(update, rules_dict):
        sorted_update = topological_sort(update, rules_dict)
        if sorted_update:
            middle_page = sorted_update[len(sorted_update) // 2]
            res += int(middle_page)
    
print(res)
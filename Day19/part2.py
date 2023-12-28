def count(part_dict, target="in"):
    if target == "R":
        return 0
    if target == "A":
        product = 1
        for lo, hi in part_dict.values():
            product *= hi - lo + 1
        return product 
    
    rules, fallback = workflows_dict[target]

    total = 0
    for part, cmp, n, workflow in rules:
        lo, hi = part_dict[part]
        if cmp == ">":
            T = [max(n+1, lo), hi]
            F = [lo, min(n, hi)]
        if cmp == "<":
            T = [lo, min(n-1, hi)]
            F = [max(n, lo), hi]
        if T[0] <= T[1]:
            copy = dict(part_dict)
            copy[part] = T
            total += count(copy, workflow)
        if F[0] <= F[1]:
            part_dict[part] = F
        else:
            break
    else:
        total += count(part_dict, fallback)
    return total

with open("Day19\input.txt", "r") as file:
    workflows, _ = file.read().split("\n\n")
workflows = workflows.split("\n")

workflows_dict = {}
for workflow in workflows:
    key = workflow[:workflow.index("{")]
    workflow_list = tuple(workflow[workflow.index("{")+1 : -1].split(","))
    value = ([], workflow_list[-1])
    for workflow in workflow_list[:-1]:
        value[0].append((workflow[0], workflow[1], int(workflow[2:workflow.index(":")]), workflow[workflow.index(":")+1:]))
    workflows_dict[key] = value

part_dict = {"x" : [1, 4000],
            "m" : [1, 4000],
            "a" : [1, 4000],
            "s" : [1, 4000]}

print(count(part_dict))





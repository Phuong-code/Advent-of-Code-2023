with open("Day19\input.txt", "r") as file:
    workflows, parts = file.read().split("\n\n")
workflows = workflows.split("\n")
parts = parts.split("\n")

workflows_dict = {}
for workflow in workflows:
    key = workflow[:workflow.index("{")]
    value = workflow[workflow.index("{")+1 : -1].split(",")
    workflows_dict[key] = value

result = 0
for part in parts:
    part_dict = {}
    part = part[1:-1]
    ratings = part.split(",")
    for rating in ratings:
        part_dict[rating[0]] = int(rating[2:])
    cur_workflow = "in"
    while True:
        if cur_workflow == "A":
            for value in part_dict.values():
                result += value
            break
        if cur_workflow == "R":
            break
        for condition in workflows_dict[cur_workflow]:
            if len(condition) > 3:
                if condition[1] == "<":
                    if part_dict[condition[0]] < int(condition[2:condition.index(":")]):
                        cur_workflow = condition[condition.index(":")+1:]
                        break
                    else:
                        continue
                elif condition[1] == ">":
                    if part_dict[condition[0]] > int(condition[2:condition.index(":")]):
                        cur_workflow = condition[condition.index(":")+1:]
                        break
                    else:
                        continue
            else:
                cur_workflow = condition
                break

print(result)
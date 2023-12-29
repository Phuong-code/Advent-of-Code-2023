import math
from functools import reduce

with open("Day20\input.txt", "r") as file:
    content = file.read().split("\n")

config_dict = {}
for line in content:
    source, destination = line.split(" -> ")
    destination = destination.split(", ")
    config_dict[source] = destination

ff_dict = {}
conjun_dict = {}
for key in config_dict:
    if key[0] == "%":
        ff_dict[key[1:]] = "off"
    if key[0] == "&":
        conjun_dict[key[1:]] = []
        for key2, val in config_dict.items():
            if key[1:] in val:
                conjun_dict[key[1:]].append([key2[1:], "low"])

for key in list(config_dict.keys()):
    if key != "broadcaster":
        val = config_dict.pop(key)
        config_dict[key[1:]] = val

for key, val in config_dict.items():
    if "rx" in val:
        conjunc_to_rx = key       

pre_conjunc_to_rx_dict ={}
for key, val in config_dict.items():
    if conjunc_to_rx in val:
        pre_conjunc_to_rx_dict[key] = 0   

time = 0
running = True
while running:
    time += 1
    queue = [("broadcaster", "low")]
    while queue:
        for conjunc in pre_conjunc_to_rx_dict:
            if (conjunc,"high") in queue:
                pre_conjunc_to_rx_dict[conjunc] = time
                break
        if all(value > 0 for value in pre_conjunc_to_rx_dict.values()):
            running = False
        start, pulse = queue.pop(0)
        for dest in config_dict[start]:
            if dest in ff_dict:
                if pulse == "high":
                    continue
                else:
                    if ff_dict[dest] == "off":
                        ff_dict[dest] = "on"
                        queue.append((dest, "high"))
                    else:
                        ff_dict[dest] = "off"
                        queue.append((dest, "low"))
            if dest in conjun_dict:
                for i in range(len(conjun_dict[dest])):
                    if conjun_dict[dest][i][0] == start:
                        conjun_dict[dest][i][1] = pulse
                        break
                for ff, pulse2 in conjun_dict[dest]:
                    if pulse2 == "low":
                        queue.append((dest, "high"))
                        break
                else:
                    queue.append((dest, "low"))

result = reduce(math.lcm, pre_conjunc_to_rx_dict.values())
print(result)

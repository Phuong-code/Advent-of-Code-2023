def get_dict(line_list, gear_list):
    dict = {}
    for i_line in range(1, len(line_list)-1):
        valid_number = ""
        valid_check = False
        for i_char in range(1, len(line_list[i_line])):
            if line_list[i_line][i_char].isdigit():
                valid_number += line_list[i_line][i_char]
                if line_list[i_line-1][i_char-1] == "*":  # top-left
                    gear_location = [i_line-1, i_char-1]
                    valid_check = True
                elif line_list[i_line-1][i_char] == "*":  # top
                    gear_location = [i_line-1, i_char]
                    valid_check = True
                elif line_list[i_line-1][i_char+1] == "*":  # top-right
                    gear_location = [i_line-1, i_char+1]
                    valid_check = True
                elif line_list[i_line][i_char-1] == "*":  # left
                    gear_location = [i_line, i_char-1]
                    valid_check = True
                elif line_list[i_line][i_char+1] == "*":  # right
                    gear_location = [i_line, i_char+1]
                    valid_check = True
                elif line_list[i_line+1][i_char-1] == "*":  # bottom-left
                    gear_location = [i_line+1, i_char-1]
                    valid_check = True
                elif line_list[i_line+1][i_char] == "*":  # bottom
                    gear_location = [i_line+1, i_char]
                    valid_check = True
                elif line_list[i_line+1][i_char+1] == "*":  # bottom-right
                    gear_location = [i_line+1, i_char+1]
                    valid_check = True
            else:
                if (valid_check == True):
                    # gear_list.index(gear_location)
                    key = gear_list.index(gear_location)
                    if (key in dict):
                        dict[gear_list.index(gear_location)].append(int(valid_number))
                    else:
                        dict[gear_list.index(gear_location)] = []
                        dict[gear_list.index(gear_location)].append(int(valid_number))
                    valid_number = ""
                    valid_check = False
                else:
                    valid_number = ""
    return dict

def get_gear_location(line_list):
    gear_list = []
    for i_line in range(1, len(line_list)-1):
        for i_char in range(0, len(line_list[i_line])):
            if line_list[i_line][i_char] == "*":
                gear_list.append([i_line, i_char])
    return gear_list

def adding_border(line_list):
    for i in range(0, len(line_list)):
        line_list[i] = "."+line_list[i].replace("\n", "")+"."
    border_top_bottom = (len(line_list[0]))*"."
    line_list.insert(0, border_top_bottom)
    line_list.append(border_top_bottom)
    return line_list

def get_sum(dict):
    sum = 0
    for val in dict.values():
        if len(val) > 1:
            power = 1
            for number in val:
                power *= number
            sum += power
    return sum


file = open("Day3\input.txt", "r")
content = file.readlines()
# print(content)
file.close()
filtered_input = adding_border(content)
gear_list = get_gear_location(filtered_input)
# print(get_gear_location(adding_border(content)))
gear_dict = get_dict(filtered_input, gear_list)
print(get_sum(gear_dict))
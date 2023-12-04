def adding_border(line_list):
    for i in range(0, len(line_list)):
        line_list[i] = "."+line_list[i].replace("\n", "")+"."
    border_top_bottom = (len(line_list[0]))*"."
    line_list.insert(0, border_top_bottom)
    line_list.append(border_top_bottom)
    return line_list

def get_sum(line_list):
    sum = 0
    for i_line in range(1, len(line_list)-1):
        valid_number = ""
        valid_check = False
        for i_char in range(1, len(line_list[i_line])):
            if line_list[i_line][i_char].isdigit():
                valid_number += line_list[i_line][i_char]
                if ((not line_list[i_line-1][i_char-1].isdigit()) and not (line_list[i_line-1][i_char-1] == ".") or # top-left
                    (not line_list[i_line-1][i_char].isdigit()) and not (line_list[i_line-1][i_char] == ".") or # top
                    (not line_list[i_line-1][i_char+1].isdigit()) and not (line_list[i_line-1][i_char+1] == ".") or # top-right
                    (not line_list[i_line][i_char-1].isdigit()) and not (line_list[i_line][i_char-1] == ".") or #left
                    (not line_list[i_line][i_char+1].isdigit()) and not (line_list[i_line][i_char+1] == ".") or #right
                    (not line_list[i_line+1][i_char-1].isdigit()) and not (line_list[i_line+1][i_char-1] == ".") or #bottom-left
                    (not line_list[i_line+1][i_char].isdigit()) and not (line_list[i_line+1][i_char] == ".") or #bottom
                    (not line_list[i_line+1][i_char+1].isdigit()) and not (line_list[i_line+1][i_char+1] == ".")): #bottom-right
                    valid_check = True
            else:
                if (valid_check == True):
                    sum += int(valid_number)
                    valid_number = ""
                    valid_check = False
                else:
                    valid_number = ""
    return sum


file = open("Day3\input.txt", "r")
content = file.readlines()
# print(content)
file.close()

print(get_sum(adding_border(content)))

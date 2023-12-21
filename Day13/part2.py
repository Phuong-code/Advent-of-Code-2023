def check_column(block):
    num_columns = len(block[0])

    for mid_col in range(num_columns - 1):
        left, right = mid_col, mid_col + 1
        is_symmetric = True
        number_of_changes = 1

        while left >= 0 and right < num_columns:
            for row in block:
                if row[left] != row[right]:
                    number_of_changes -= 1
                    if number_of_changes < 0:
                        is_symmetric = False
                        break
            if not is_symmetric:
                break
            left -= 1
            right += 1

        if is_symmetric and number_of_changes == 0:
            return mid_col + 1
    return 0


def check_row(block):
    rows, cols = len(block), len(block[0])
    block = [[block[j][i] for j in range(rows)] for i in range(cols)]
    return check_column(block)


file = open("Day13\input.txt", "r")
content = file.read()
file.close()
blocks = content.split("\n\n")

sum = 0
for i in blocks:
    block = i.split("\n")
    sum += check_column(block) + check_row(block)*100
print(sum)

# 23479 correct answer
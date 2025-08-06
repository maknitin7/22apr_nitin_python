rows = 6
cols = 4

for i in range(1, rows + 1):
    line = ""
    for j in range(1, cols + 1):
        if i == 1 or i == rows or j == 1 or j == cols:
            line = line + "*"
        else:
            line = line + " "
    print(line)

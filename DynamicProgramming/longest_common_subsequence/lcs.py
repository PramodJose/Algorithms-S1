INP_FILE = "input.dat"


def print_lcs(table, x, y):
    i = len(y)
    j = len(x)
    st = ""

    while i != 0 and j != 0:
        if table[i-1][j] == table[i][j-1]:
            cur_val = table[i][j]
            i -= 1
            j -= 1
            if table[i][j] != cur_val:
                st = x[j] + st
        elif table[i-1][j] < table[i][j-1]:
            j -= 1
        else:
            i -= 1
    print(st)


def lcs(x, y):
    len_x = len(x)
    len_y = len(y)
    table = []

    for i in range(len_y + 1):
        row = [0] * (len_x + 1)
        table.append(row)

    for i in range(len_y):
        for j in range(len_x):
            if y[i] == x[j]:
                table[i + 1][j + 1] = table[i][j] + 1
            else:
                table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j])
    print_lcs(table, x, y)

    return table[len_y][len_x]


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    x = fin.readline()[:-1]
    y = fin.readline()[:-1]
    fin.close()
    print(lcs(x, y))

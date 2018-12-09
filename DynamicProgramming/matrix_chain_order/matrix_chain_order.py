INP_FILE = "input.dat"


def print_order(start, length, splits, names):
    if length == 1:
        return names[start]
    elif length == 2:
        return "(" + names[start] + " " + names[start + 1] + ")"

    split_point = splits[start + 1, start + length]
    left_length = split_point - start
    right_length = length - left_length
    left = print_order(start, left_length, splits, names)
    right = print_order(split_point, right_length, splits, names)

    if length == len(names):
        return left + right
    else:
        return "(" + left + right + ")"


def find_order(dimensions, matrices_count, names):
    table = {}
    splits = {}

    for i in range(1, matrices_count + 1):     # diagonals are all 0
        table[i, i] = 0

    for l in range(2, matrices_count + 1):
        for i in range(1, matrices_count - l + 2):
            j = i + l - 1
            table[i, j] = None
            for k in range(i, j):
                cost = table[i, k] + table[k + 1, j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if table[i, j] is None or cost < table[i, j]:
                    table[i, j] = cost
                    splits[i, j] = k

    print("The cost is: ", table[1, matrices_count])
    order = print_order(0, matrices_count, splits, names)
    print("And the order is: ", order)


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    dimensions = fin.readline().split()
    names = fin.readline().split()
    fin.close()
    dim_count = len(dimensions)
    for i in range(dim_count):
        dimensions[i] = int(dimensions[i])

    find_order(dimensions, dim_count - 1, names)

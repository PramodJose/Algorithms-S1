INP_FILE = "input1.dat"


def knapsack(capacity, weights, profits):
    item_count = len(weights)
    table = []
    for i in range(item_count + 1):
        row = [0] * (capacity + 1)
        table.append(row)

    for i in range(1, item_count + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                table[i][w] = max(table[i-1][w], table[i - 1][w - weights[i - 1]] + profits[i - 1])
            else:
                table[i][w] = table[i-1][w]

    return table[item_count][capacity]


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    weights = fin.readline().split()
    profits = fin.readline().split()
    capacity = int(fin.readline())
    fin.close()

    items = len(weights)
    for i in range(items):
        weights[i] = int(weights[i])
        profits[i] = int(profits[i])

    print(knapsack(capacity, weights, profits))

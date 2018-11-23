INP_FILE = "input.dat"


def make_change():
    fin = open(INP_FILE, "r")
    total_value = int(fin.readline().split()[0])
    denominations = fin.readline().split()
    fin.close()

    costs = list()
    costs.append([])
    for i in range(total_value + 1):
        costs[0].append(i)

    for i in range(1, len(denominations)):      # i is the row
        costs.append([0])
        cost = int(denominations[i])

        for j in range(1, total_value + 1):     # j is the column
            not_taking_it = costs[i-1][j]

            if j < cost:
                costs[i].append(not_taking_it)
            else:
                taking_it = 1 + costs[i][j - cost]
                costs[i].append(min(not_taking_it, taking_it))

    return costs[len(denominations) - 1][total_value]


if __name__ == "__main__":
    print(make_change())

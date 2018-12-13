INP_FILE = "input2.dat"


class Item:
    def __init__(self, wt, gain):
        self.weight = wt
        self.profit = gain
        self.profit_unit_weight = gain/wt

    def __lt__(self, other):
        return self.profit_unit_weight < other.profit_unit_weight


def frac_knapsack(items, capacity):
    items = sorted(items, reverse=True)
    current_weight = 0
    profit = 0
    item_no = 0

    while current_weight < capacity:
        if current_weight + items[item_no].weight <= capacity:
            current_weight += items[item_no].weight
            profit += items[item_no].profit
        else:
            remaining_weight = capacity - current_weight
            profit += (remaining_weight / items[item_no].weight) * items[item_no].profit
            current_weight += remaining_weight
        item_no += 1

    print("The maximum profit is", profit)
    return profit


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    weights = fin.readline().split()
    profits = fin.readline().split()
    capacity = int(fin.readline())
    fin.close()

    items_count = len(weights)
    items = []
    for i in range(items_count):
        items.append(Item(int(weights[i]), int(profits[i])))

    frac_knapsack(items, capacity)

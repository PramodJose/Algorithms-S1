INP_FILE = "input.dat"
import heapq


class HeapNode:
    def __init__(self, sym, freq):
        self.symbol = sym
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def get_encodings(root, encoding_dict, path_code=""):
    if root.left is None and root.right is None:
        encoding_dict[root.symbol] = path_code
    else:
        get_encodings(root.left, encoding_dict, path_code + "0")
        get_encodings(root.right, encoding_dict, path_code + "1")


def huffman(char_heap):
    heapq.heapify(char_heap)

    while len(char_heap) != 1:
        left = heapq.heappop(char_heap)             # obtain the minimum (which goes on the left, by convention)..
        right = heapq.heappop(char_heap)            # ..and the second minimum (which goes on the right, by convention).
        combined = HeapNode(left.symbol+"+"+right.symbol, left.freq + right.freq)    # combine them into a new node.
        combined.left = left                                # make the new node point to the left..
        combined.right = right                              # ..and right nodes..
        heapq.heappush(char_heap, combined)                 # ..and push the new node back to the min-heap.

    root = char_heap[0]
    encoding_dict = dict()
    get_encodings(root, encoding_dict)
    return encoding_dict


if __name__ == "__main__":
    fin = open(INP_FILE, "r")
    chars = fin.readline().split()
    freqs = fin.readline().split()
    fin.close()

    char_heap = []
    char_count = len(chars)
    for i in range(char_count):
        char_heap.append(HeapNode(chars[i], int(freqs[i])))

    print(huffman(char_heap))

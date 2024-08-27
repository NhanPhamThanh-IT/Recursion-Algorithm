# This program works by identifying the remaining elements and backtrack only on those.
# The elements are inserted in the increasing order of the elements left to be inserted. And hence runs much faster.
# Comparing with other back tracking algorithms, it runs 5X faster.

# Input matrix
arr = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

# Position of the input elements in the arr
# pos = {
#     element: [[position 1], [position 2]]
# }
pos = {}

# Count of the remaining number of the elements
# rem = {
#     element: pending count
# }
rem = {}

# Graph defining tentative positions of the elements to be filled
# graph = {
#     key: {
#         row1: [columns],
#         row2: [columns]
#     }
# }
graph = {}


# Print the matrix array
def printMatrix():
    for i in range(0, 9):
        for j in range(0, 9):
            print(str(arr[i][j]), end=" ")
        print()


# Method to check if the inserted element is safe
def is_safe(x, y):
    key = arr[x][y]
    for i in range(0, 9):
        if i != y and arr[x][i] == key:
            return False
        if i != x and arr[i][y] == key:
            return False

    r_start = int(x / 3) * 3
    r_end = r_start + 3

    c_start = int(y / 3) * 3
    c_end = c_start + 3

    for i in range(r_start, r_end):
        for j in range(c_start, c_end):
            if i != x and j != y and arr[i][j] == key:
                return False
    return True


# method to fill the matrix
# input keys: list of elements to be filled in the matrix
#        k   : index number of the element to be picked up from keys
#        rows: list of row index where element is to be inserted
#        r   : index number of the row to be inserted
#
def fill_matrix(k, keys, r, rows):
    for c in graph[keys[k]][rows[r]]:
        if arr[rows[r]][c] > 0:
            continue
        arr[rows[r]][c] = keys[k]
        if is_safe(rows[r], c):
            if r < len(rows) - 1:
                if fill_matrix(k, keys, r + 1, rows):
                    return True
                else:
                    arr[rows[r]][c] = 0
                    continue
            else:
                if k < len(keys) - 1:
                    if fill_matrix(k + 1, keys, 0, list(graph[keys[k + 1]].keys())):
                        return True
                    else:
                        arr[rows[r]][c] = 0
                        continue
                return True
        arr[rows[r]][c] = 0
    return False


# Fill the pos and rem dictionary. It will be used to build graph
def build_pos_and_rem():
    for i in range(0, 9):
        for j in range(0, 9):
            if arr[i][j] > 0:
                if arr[i][j] not in pos:
                    pos[arr[i][j]] = []
                pos[arr[i][j]].append([i, j])
                if arr[i][j] not in rem:
                    rem[arr[i][j]] = 9
                rem[arr[i][j]] -= 1

    # Fill the elements not present in input matrix. Example: 1 is missing in input matrix
    for i in range(1, 10):
        if i not in pos:
            pos[i] = []
        if i not in rem:
            rem[i] = 9

# Build the graph


def build_graph():
    for k, v in pos.items():
        if k not in graph:
            graph[k] = {}

        row = list(range(0, 9))
        col = list(range(0, 9))

        for cord in v:
            row.remove(cord[0])
            col.remove(cord[1])

        if len(row) == 0 or len(col) == 0:
            continue

        for r in row:
            for c in col:
                if arr[r][c] == 0:
                    if r not in graph[k]:
                        graph[k][r] = []
                    graph[k][r].append(c)


build_pos_and_rem()

# Sort the rem map in order to start with smaller number of elements to be filled first. Optimization for pruning
rem = {k: v for k, v in sorted(rem.items(), key=lambda item: item[1])}

build_graph()

key_s = list(rem.keys())
# Util called to fill the matrix
fill_matrix(0, key_s, 0, list(graph[key_s[0]].keys()))

printMatrix()
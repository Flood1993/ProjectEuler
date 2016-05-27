import copy

def improvedResult(x, y):
    res = False

    if x > 0:
        if shortestPaths[x - 1][y] + matrix[x][y] < shortestPaths[x][y]:
            shortestPaths[x][y] = shortestPaths[x - 1][y] + matrix[x][y]
            res = True

    """if y < len(shortestPaths[0]) - 1:
        if shortestPaths[x][y + 1] + matrix[x][y] < shortestPaths[x][y]:
            shortestPaths[x][y] = shortestPaths[x][y + 1] + matrix[x][y]
            res = True"""

    if y > 0:
        if shortestPaths[x][y - 1] + matrix[x][y] < shortestPaths[x][y]:
            shortestPaths[x][y] = shortestPaths[x][y - 1] + matrix[x][y]
            res = True

    if x < len(shortestPaths) - 1:
        if shortestPaths[x + 1][y] + matrix[x][y] < shortestPaths[x][y]:
            shortestPaths[x][y] = shortestPaths[x + 1][y] + matrix[x][y]
            res = True

    return res

#example solution should be: 2297

matrix = []

# read file and store it in matrix
with open("./p082_matrix.txt") as f:
    content = f.readlines()

    for line in content:
        val = line.split(",")
        for i in range(0, len(val)):
            val[i] = int(val[i])

        matrix.append(val)

shortestPaths = copy.deepcopy(matrix)

# set shortest paths to 1000000, except for the start cell
for i in range(0, len(shortestPaths)):
    for j in range(0, len(shortestPaths[0])):
        if j == 0:
            continue
        shortestPaths[i][j] = 1000000

somethingChanged = True

while somethingChanged:
    somethingChanged = False
    for i in range(0, len(shortestPaths)):
        for j in range(0, len(shortestPaths[0])):
            somethingChanged = somethingChanged or improvedResult(i, j)

print(shortestPaths)

min = 1000000
for i in range(0, len(shortestPaths)):
    if shortestPaths[i][len(shortestPaths) - 1] < min:
        min = shortestPaths[i][len(shortestPaths) - 1]

print (min)
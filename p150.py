#p150

# Example triangle
X = [[15], [-14, -7], [20, -13, -5], [-3, 8, 23, -26], [1, -4, -5, -18, 5], [-16, 31, 2, 9, 28, 3]]

# Generate the good triangle now
t = 0
myMod = 2**20
sub = 2**19
def getNextNumber():
    global t
    t = (615949*t + 797807)%myMod
    return t - sub

X = []
for i in range(1, 501): # TODO: set this to 1001
    toAdd = []
    for j in range(i):
        toAdd.append(getNextNumber())
    X.append(toAdd)
print("Triangle generated successfully")

# Function used to calculate the sum of a subtriangle, from a given position
def sumTri(L, row, pos, deep):
    res = L[row][pos]
    for i in range(1, deep + 1):
        for j in range(i + 1):
            res += L[row + i][pos + j]
    return res

# Create the final triangle
sol = []
for i in range(1, len(X)+1):
    toAdd =  []
    for k in range(i):
        toAdd.append([0, 0])
    sol.append(toAdd)

# Create the tmp structure to hold the sums for a given position with a given depth
partialSums = []
for i in range(1, len(X)+1):
    toAdd =  []
    for k in range(i):
        toAdd.append([0, 0])
    partialSums.append(toAdd)

# fill last row of solution with values
lastRow = sol[len(sol) - 1]
for i in range(len(lastRow)):
    lastRow[i][0] = X[len(X) - 1][i]

# fill last row of solution with values
lastPartialSums = partialSums[len(partialSums) - 1]
for i in range(len(lastPartialSums)):
    lastPartialSums[i][0] = X[len(X) - 1][i]

# Bottom up approach
for i in range(len(sol) - 2, -1, -1):
    print(i)
    for j in range(len(sol[i])):
        maxDepth = max(sol[i+1][j][1], sol[i+1][j+1][1])

        val = X[i][j] + partialSums[i + 1][j + 1][0]
        for k in range(0, maxDepth + 1):
            #print("\t", k)
            val += X[i + k + 1][j]

        if (val < X[i][j]):
            sol[i][j] = [val, maxDepth + 1]
            partialSums[i][j] = [val, maxDepth + 1]
        else:
            sol[i][j] = [X[i][j], 0]
            partialSums[i][j] = [X[i][j], 0]
        #print(i, j, val, maxDepth)

# TDD
print(sol[0][0], "should be", -25)
print(sol[1][1], "should be", -20)
print(sol[2][2], "should be", -42)

"""
print("sol")
for row in sol:
    print(row)
print("partialSums")
for row in partialSums:
    print(row)
"""

print("Calculating lowest")

# Print lowest value
lowest = 80000000
for row in sol:
    for pos in row:
        if pos[0] < lowest:
            lowest = pos[0]

print("lowest", lowest)
print("first", getNextNumber())
print("first", getNextNumber())

"""
# Print triangles in readable format
for row in sol:
    print(row)
for row in X:
    print(row)
"""
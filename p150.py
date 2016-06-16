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
for i in range(1, 1001): # TODO: set this to 1001
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

# fill last row of solution with values
lastRow = sol[len(sol) - 1]
for i in range(len(lastRow)):
    lastRow[i][0] = X[len(X) - 1][i]


# Bottom up approach
for i in range(len(sol) - 2, -1, -1):
    if i%25 == 0:
        print(i)
    for j in range(len(sol[i])):
        # We have to check both subtriangles and all of them in between on every step

        # Find lowest depth value
        leftDepth = sol[i + 1][j][1]
        rightDepth = sol[i + 1][j + 1][1]
        diff = int(abs(leftDepth - rightDepth))

        if leftDepth == 0 and rightDepth == 0:
            # Just check those values
            val = X[i][j] + sol[i + 1][j][0] + sol[i + 1][j + 1][0]

            if val <= X[i][j]:
                sol[i][j] = [val, 1]
            else:
                sol[i][j] = [X[i][j], 0]

        elif leftDepth == rightDepth:
            val = X[i][j] + sol[i + 1][j + 1][0]
            depth = sol[i + 1][j + 1][1]

            for k in range(0, depth + 1):
                val += X[i + k + 1][j]

            if val <= X[i][j]:
                sol[i][j] = [val, depth + 1]
            else:
                sol[i][j] = [X[i][j], 0]

        elif leftDepth < rightDepth:
            val = X[i][j] + sol[i + 1][j][0]
            depth = sol[i + 1][j][1]

            for k in range(0, depth + 1):
                val += X[i + k + 1][j + k + 1]
            
            if val <= X[i][j]:
                sol[i][j] = [val, depth + 1]
            else:
                sol[i][j] = [X[i][j], 0]

            tmp = 0
            if i != len(sol) - 2:
                tmp = sol[i+2][j+1][1]
            q = depth + 2
            while q < max(rightDepth + 2, tmp+3):
                for w in range(0, q + 1):
                    val += X[i + q][j + w]

                if val <= sol[i][j][0]:
                    sol[i][j] = [val, q]

                q += 1

        elif leftDepth > rightDepth:
            val = X[i][j] + sol[i + 1][j + 1][0]
            depth = sol[i + 1][j + 1][1]

            for k in range(0, depth + 1):
                val += X[i + k + 1][j]
            
            if val <= X[i][j]:
                sol[i][j] = [val, depth + 1]
            else:
                sol[i][j] = [X[i][j], 0]

            tmp = 0
            if i != len(sol) - 2:
                tmp = sol[i+2][j+1][1]
            q = depth + 2
            while q < max(leftDepth + 2, tmp + 3):
                for w in range(0, q + 1):
                    val += X[i + q][j + w]

                if val <= sol[i][j][0]:
                    sol[i][j] = [val, q]

                q += 1
            
            

        """
        # Go adding rows until the biggest depth value

        # Keep the best value

        # Check considering right subtriangle
        val = X[i][j] + sol[i + 1][j + 1][0]
        depth = sol[i + 1][j + 1][1]

        for k in range(0, depth + 1):
            val += X[i + k + 1][j]

        if (val <= X[i][j]):
            # The total sum obtained for that position is lower
            sol[i][j] = [val, depth + 1]
        else:
            sol[i][j] = [X[i][j], 0]

        # Check considering left subtriangle
        val = X[i][j] + sol[i + 1][j][0]
        depth = sol[i + 1][j][1]

        for k in range(0, depth + 1):
            val += X[i + k + 1][j + k + 1]

        if (val < sol[i][j][0]):
            # The total sum obtained for that position is lower
            sol[i][j] = [val, depth + 1]

        # Check all the intermediate triangles between the two
        diff = abs(sol[i + 1][j][1] - sol[i + 1][j + 1][1])
        if diff != 0:
            # Different depths
            leftDeeper = sol[i + 1][j][1] > sol[i + 1][j + 1][1]
            if leftDeeper:
                val = X[i][j] + sol[i + 1][j + 1][0]
                depth = sol[i + 1][j + 1][1]

                for k in range(0, depth + 1):
                    val += X[i + k + 1][j]

                for i in range()


            else:
                # Right subtriangle deeper
                val = X[i][j] + sol[i + 1][j][0]
                depth = sol[i + 1][j][1]

                for k in range(0, depth + 1):
                    val += X[i + k + 1][j + k + 1]

        #else:
        #    sol[i][j] = [X[i][j], 0]
        """

# TDD
print(sol[0][0][0], "should be", -23)
print(sol[1][1][0], "should be", -42)

"""
print("sol")
for row in sol:
    print(row)
"""

print("Calculating lowest")

# Print lowest value
lowest = 80000000
for row in sol:
    for pos in row:
        if pos[0] < lowest:
            lowest = pos[0]

print("Lowest:", lowest)
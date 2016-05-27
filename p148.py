def addRow():
    tmp = [1]
    lastRow = len(pascalTriangle) - 1
    for i in range (0, len(pascalTriangle[lastRow]) - 1):
        tmp.append(pascalTriangle[lastRow][i] + pascalTriangle[lastRow][i + 1])
    tmp.append(1)
    pascalTriangle.append(tmp)

pascalTriangle = []
pascalTriangle.append([1])
pascalTriangle.append([1, 1])

for i in range(0, 98):
    addRow()

totalDivisible = 0

for i in range(0, len(pascalTriangle)):
    divBySevenCount = 0
    for element in pascalTriangle[i]:
        if element%7 == 0:
            divBySevenCount += 1
    totalDivisible += divBySevenCount
    print("Row: " + str(i) + ". Divs by 7: " + str(divBySevenCount))

print(totalDivisible)

"""
Conclusions:

It seems that for numbers of the form:
    - 7k     -> the number of multiples of 7 is 6k
    - 7k + 1 -> the number of multiples of 7 is 5k
    - 7k + 2 -> the number of multiples of 7 is 4k
    - 7k + 3 -> the number of multiples of 7 is 3k
    - 7k + 4 -> the number of multiples of 7 is 2k
    - 7k + 5 -> the number of multiples of 7 is 1k
    - 7k + 6 -> the number of multiples of 7 is 0

    ! ! WRONG ! ! Check current output and keep investigating

    7 would be k = 1
    98 would be k = 14
"""

"""
def tri(n):
    return n*(n+1)/2

def cntr(n):
    if n < 7:
        return 0
    if n % 7 == 0:
        return 6*int(n/7)
    if n % 7 == 1:
        return 5*int(n/7)
    if n % 7 == 2:
        return 4*int(n/7)
    if n % 7 == 3:
        return 3*int(n/7)
    if n % 7 == 4:
        return 2*int(n/7)
    if n % 7 == 5:
        return 1*int(n/7)
    if n % 7 == 6:
        return 0

myTMP = 0

for i in range(0, 100):
    myTMP += cntr(i)

print(myTMP)

res = tri(100) - (21*tri(15) + 6*15 + 5*15 + 4*15)

print(res)
print(tri(100))
print(93/7)
print(93%7)
"""
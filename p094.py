import math
import numbers

#Given the standard lenght of a side, returns the area of the triangle having one side one unit longer
def areaplus(n):
    return (n+1) * math.sqrt(3*n**2 - 2*n - 1)/4
    
for i in range(5, 50):
    print areaplus(i)
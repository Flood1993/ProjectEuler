import numpy as np
import time

f = open('triangles.txt', 'r')
# f contains the triangles

def sameside(p1,p2, a,b):
    #Returns if two points are in the same side of a vector
    #First two parameters are the points to check, the last two are the points that give you the vector
    cp1 = np.cross(b-a, p1-a)
    cp2 = np.cross(b-a, p2-a)
    if np.dot(cp1, cp2) >= 0:
        return True
    return False

def pointintriangle(p, a,b,c):
    #Returns if a point p is contained in the triangle [a,b,c]
    if sameside(p,a, b,c) and sameside(p,b, a,c) and sameside(p,c, a,b): 
        return True
    return False
    
P = np.matrix('0, 0')

total = 0

start_time = time.time()

for i in range(0, 1000):
    triangle = f.readline()
    #Leemos la siguiente linea (el siguiente triangulo)

    arrtri = triangle.split(',')
    #Creamos un array separando cada elemento segun las comas del array

    A = np.matrix(arrtri[0] + ',' + arrtri[1])
    B = np.matrix(arrtri[2] + ',' + arrtri[3])
    C = np.matrix(arrtri[4] + ',' + arrtri[5])
    #Creamos los 3 puntos del triangulo
    
    if pointintriangle(P, A, B, C):
        total += 1
        
print total

print time.time() - start_time, "seconds"
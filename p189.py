"""
Para 2 filas es 24 = 3 * 2**3

Para 3 filas es 528 = 11 * 3 * 2**4

Para 4 filas es 31968 = 37 * 3**3 * 2**5

Para 2 filas es 24, se puede comprobar a mano

Para 3 filas es 528, porque sabiendo que hay 24 para el nivel anterior, hay 2 triangulos que estarán conectados con el nuevo nivel. Esos dos triángulos, dependiendo de los 2 de arriba:

En un tercio de los casos, serán iguales
    Si son iguales, quiere decir que 1/2 de las veces el de en medio vendrá fijo, y 1/2 de las veces será a elegir entre 2
En dos tercios de los casos, serán diferentes, lo que significa que el de siempre siempre vendrá fijo
"""

L = [3, 24, 528, 31968]

for i in range(1, len(L)):
    for j in range(i):
        print(L[i], L[j], L[i]/L[j])

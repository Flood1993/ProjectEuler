A = []

#Creamos una lista con todos los cuadrados del uno al 10000
for i in range(1, 10000):
	A.append(i*i)

print len(A) # 9999??
#Empezando por el 1, vamos sumando cuadrados. En cada paso, miramos si el acumulado es palindromo (si lo es, lo sumamos a la solución). Sumamos hasta que la suma sea >= 10^8

TOTAL = 0

for i in range(1, 10000):
	suma = A(i)
	if (isPalindrome(suma)):
		TOTAL += suma
	#Aqui no estoy seguro de si se meteria para la ultima iteracion del bucle, COMPROBAR
	for j in range(i+1, 10000):
		suma += A(j)
		
		if (suma >= 100000000):
			continue
		if (isPalindrome(suma)):
			TOTAL += suma

print TOTAL

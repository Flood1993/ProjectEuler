from functions import totient
import sys

def resilience(n):
    return totient(n) / (n-1)

limit = 15499/94744
for i in range(1000000, int(sys.argv[1])):
    if resilience(i) < limit:
        print(i)

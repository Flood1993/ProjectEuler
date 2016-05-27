def exploreChain(n):
    chain = []
    element = n
    chain.append(element)

    while True:
        element = List[element]

        if (element > 1000000):
            return -1        
        if (element in chain):
            break

        chain.append(element)

    for i in range(0, len(chain)):
        if chain[i] == element:
            return len(chain) - 1 - i
    
    return -1

###############################

List = [1]*1000001
Checked = [False]*1000001

for i in range(2, 1000000):
    x = i+i
    while x <= 1000000:
        List[x] += i
        x += i

# Position n contains the sum of the proper divisors of n. (1 for primes)
print("Finished generating numbers")
"""
longestChainSize = -1
longestChainStarter = -1

for i in range(0, len(List)):
    current = exploreChain(i)
    if current > longestChainSize:
        longestChainSize = current
        longestChainStarter = i

print(longestChainSize)
print(longestChainStarter)
"""
# This returns 5916

x = 5916
print (x)
while (List[x] != 5916):
    x = List[x]
    print(x)
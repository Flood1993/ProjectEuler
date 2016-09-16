from functions import pythTriplet

# It seems that the perimeter of a primitive pythagorean triplet is:
# m*m + 2*m*n + m*m = 2mm + 2mn

sol_count = 0
LEN_WIRE = 50
UPPER_LIMIT = int((LEN_WIRE**0.5) + 1)

solutions = set()
checked_already = set()

for m in range(2, UPPER_LIMIT):
    for n in range(1, m): # n cannot be equal to m
        tmp = 2*m*m + 2*m*n
        val = tmp

        while tmp <= LEN_WIRE:
            if tmp == 24:
                print('AA', m, n)
            if tmp > LEN_WIRE:
                break

            if (tmp in solutions) and (tmp in checked_already):
                tmp += val
                continue

            if (tmp in solutions):
                checked_already.add(tmp)
                sol_count -= 1
                tmp += val
                continue

            solutions.add(tmp)
            sol_count += 1  
            
            tmp += val

print(sol_count)
print(len(solutions))
print(len(checked_already))

for x in solutions:
    print('solution', x)

for x in checked_already:
    print('c-a', x)



"""
3, 4, 5
6, 8, 10

8, 6, 10
"""





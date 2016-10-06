# Generate the good triangle now
t = 0
myMod = 2**20
sub = 2**19
def getNextNumber():
    global t
    t = (615949*t + 797807)%myMod
    return t - sub

L = []
for i in range(1, 1001): # TODO: set this to 1001
    toAdd = []
    for j in range(i):
        toAdd.append(getNextNumber())
    L.append(toAdd)
print("Triangle generated successfully")

smallest = 1024*1024*1024

for k in range(len(L) - 2, 1, -1):
	i = k
	
	next = [L[i+1][j] + L[i+1][j+1] + L[i][j] for j in range(i+1)]
	next2 = L[k+1]
	
	while i > 0:
		i -= 1
		tmp = [L[i][j] + next[j] + next[j+1] - next2[j+1] for j in range(i+1)]
		smallest = min(smallest, min(tmp))
		next2 = next
		next = tmp
		
print(smallest)
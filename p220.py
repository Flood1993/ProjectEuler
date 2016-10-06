st = "Fa"

for i in range(2):
	st = st.replace("a", "cRdFR")
	st = st.replace("b", "LFcLd")
	st = st.replace("c", "a")
	st = st.replace("d", "b")
	
st = st.replace("a", "")
st = st.replace("b", "")

print("elements:", len(st))
print("F's:", st.count("F"))

pos = [0, 0]
dir = 0 # 0 up, 1 right, 2 down, 3 left

cnt = 0

for el in st:
	if cnt == 500:
		break
	if el == "L":
		dir = (dir-1)%4
	elif el == "R":
		dir = (dir+1)%4
	elif el == "F":
		cnt += 1
		if dir == 0:
			pos[1] += 1
		elif dir == 1:
			pos[0] += 1
		elif dir == 2:
			pos[1] -= 1
		elif dir == 3:
			pos[0] -= 1
			
print(pos)

"""n = 1
4 els
2 F

n = 2
10 els (+6)
4 F

n = 3
22 els (+12)
8 F

n = 4
46 els (+24)
16 F

n = 5
94 els (+48)
32 F

n = 6
190 els (+96)
64 F

On iteration N, there will be

2**N F
"""
"""
70, 70, 9, 60 (1)            9*70, 70*69, 8, 60   (1 * 9/69)
 0,  0, 0,  0 (0)        70*60,70*69, 18, 50      (1 * 60/69)     (9/70)*8 + (60/69)*18, 
"""

P = [None]*140

P[0] = ((70, 70, 9, 60)) # numerator, denominator, repeated balls for next, non-repeated balls for next
P[1] = ((0, 0, 0, 0))
P[2] = ((0, 0, 0, 0))
P[3] = ((0, 0, 0, 0))
P[4] = ((0, 0, 0, 0))
P[5] = ((0, 0, 0, 0))
P[6] = ((0, 0, 0, 0))

for i in range(1, 20):
    for j in range(7):
        prev_left = P[(i-1)*7 + j]
        if j == 0:
            P[i*7] = ((prev_left[0]*prev_left[2], prev_left[1]*(prev_left[2] + prev_left[3]), prev_left[2] - 1, prev_left[3]))
            continue
        prev_topleft = P[(i-1)*7 + j-1]
        new_num = prev_topleft[0]*prev_topleft[3] + prev_left[0]*prev_left[2]
        new_denom = prev_topleft[1]*(prev_topleft[2] + prev_topleft[3])
        rep_balls = 10*(j+1) - (i+1)
        non_rep_balls = 70 - 10*(j+1)
        P[i*7 + j] = ((new_num, new_denom, rep_balls, non_rep_balls))

print(P)

res = 0
for i in range(7):
    res = res + (i+1) * P[19*7 + i][0] / P[19*7 + i][1]

print(res) 
"""P = [[[] for i in range(7)] for j in range(20)]

print(P)

P[0][0] = ((70, 70, 9, 60)) # numerator, denominator, repeated balls for next, non-repeated balls for next
P[0][1] = ((0, 0, 0, 0))
P[0][2] = ((0, 0, 0, 0))
P[0][3] = ((0, 0, 0, 0))
P[0][4] = ((0, 0, 0, 0))
P[0][5] = ((0, 0, 0, 0))
P[0][6] = ((0, 0, 0, 0))

for i in range(1, 20):
    for j in range(7):
        prev_left = P[0][i-1][j]
        if j == 0:
            P[i][j] = ((prev_left[0]*prev_left[2], prev_left[1]*(prev_left[2] + prev_left[3]), prev_left[2] - 1, prev_left[3]))
            continue
        prev_topleft = P[0][i-1][j-1]
        total_balls = prev_left[2] + prev_left[3]
        new_num = prev_topleft[0]*prev_topleft[3] + prev_left[0]*prev_left[2]
        new_denom = prev_left[1] - 1
        rep_balls = 10*(j+1) - (i+1)
        non_rep_balls = 70 - 10*(j+1)
        P[i][j] = ((new_num, new_denom, rep_balls, non_rep_balls))

print(P[1])"""
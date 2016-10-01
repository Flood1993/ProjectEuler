res = -600000000897

def above_res(r):
    tmp1 = -14100 * pow(r, 5001)
    tmp2 = 14103 * pow(r, 5000)
    tmp3 = 6 * pow(10, 11) * pow(r, 2)
    tmp4 = -12 * pow(10, 11) * r
    tmp5 = -900 * r
    return tmp1 + tmp2 + tmp3 + tmp4 + tmp5 > res

print(above_res(1))
print(above_res(2))

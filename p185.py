L = [5616185650518293,
3847439647293047,
5855462940810587,
9742855507068353,
4296849643607543,
3174248439465858,
4513559094146117,
7890971548908067,
8157356344118483,
2615250744386899,
8690095851526254,
6375711915077050,
6913859173121360,
6442889055042768,
2321386104303845,
2326509471271448,
5251583379644322,
1748270476758276,
4895722652190306,
3041631117224635,
1841236454324589,
2659862637316867]

def count(num, pos):
    tmp = str(num)
    res = 0
    for el in L:
        if str(el)[pos] == tmp:
            res += 1
    return res

for i in range(16):
    tmp = [count(x, i) for x in range(10)]
    print(tmp)

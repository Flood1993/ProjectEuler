numbers = [pow(290797, 2, 50515093)]

for i in range(19999):
    numbers.append(pow(numbers[-1], 2, 50515093))

for i in range(len(numbers)):
    numbers[i] = numbers[i]%500

def have_TIP(s1, s2):
    a, b = s1
    c, d = s2
    return check_different_sides(a,b,c,d) and check_different_sides(c,d,a,b)

def check_different_sides(a, b, c, d):
    AB = (b[0] - a[0], b[1] - a[1])
    AC = (c[0] - a[0], c[1] - a[1])
    AD = (d[0] - a[0], d[1] - a[1])

    p1 = AB[0]*AC[1] - AB[1]*AC[0]
    p2 = AB[0]*AD[1] - AB[1]*AD[0]

    return p1*p2 < 0

print(numbers[:4])

segments = []

for i in range(5000):
    a = (numbers[4*i], numbers[4*i + 1])
    b = (numbers[4*i + 2], numbers[4*i + 3])
    s = (a,b)
    segments.append(s)

print("Segments added OK", len(segments), segments[0])

t_i = 0

for i in range(len(segments)):
    for j in range(i + 1, len(segments)):
        if have_TIP(segments[i], segments[j]):
            t_i += 1

print(t_i)

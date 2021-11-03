from math import ceil
from collections import defaultdict
from functions import factorial

'''
I'm not doing it right: Not counting properly the multi-layered layers.

Let's think in one lower dimension

On 1D, we need 2 blocks for layer N of a cuboid of dimensions x
            #######     k = 6 blocks

           ·#######·    layer 1 = 2 blocks needed


On 2D, we need ? blocks for layer N of a cuboid of dimensions x*y
2*3 = 6 blocks

            ###         x = 3, y = 2
            ###

            ···         layer 1
           ·###·        needed 2*3 + 2*2 + 4*0 = 10 blocks
           ·###·
            ···

            ···
           ·###·         layer 2
          ·#####·        needed 2*3 + 2*2 + 4*1 = 14 blocks
          ·#####·
           ·###·
            ···

            It seems that for layer n, we need (2*x + 2*y + 4*(l-1)) blocks to recover and so that it origins from a valid cuboid

            So, for a number of n blocks, if it satisfies 2*x + 2*y + 4*(l - 1) == n, for some x, y, l, then we know it's a valid wrap

On 3D
        x = 3, y = 2, z = 1

            layer 1
            needs 2 * 3*2 + 2 * 3*1 + 2 * 2*1 = 22 blocks

            layer 2
            needs 2 * 3*2 + 2 * 3*1 + 2 * 2*1 + 4 * 3 + 4 * 2 + 4 * 1 = 22 + 12 + 8 + 4 = 46        46-22 = 24
                            base + 4 (x+y+z)

            layer 3
            needs 2 * 3*2 + 2 * 3*1 + 2 * 2*1 + 2*4*3*1 + 2*4*2*1 + 2*4*1*1 = 22 + 24 + 16 + 8 = 54 + 16 = 70    (8 missing)?      78-46 = 32

            layer 4
            118-78 = 40
'''


def C(n):
    set_sols = defaultdict(int)
    result = 0
    for x in range(1, n):
        for y in range(1, x + 1):
            x_times_y = x*y
            if x_times_y > n:
                break
            for z in range(1, y + 1):
                if x_times_y * z > n:
                    break
                layer = 1
                blocks = blocks_needed(x, y, z, layer)
                while blocks < n:
                    layer = layer + 1
                    blocks = blocks_needed(x, y, z, layer)
                if blocks == n:
                    # print(f'Valid solution for {n}: ({x}, {y}, {z}, {layer})')
                    result = result + 1

    return result
    # suppose n == 22
    '''
    algorithm: start from middle layer, and fill outwards, where layers can only become smaller or stay the same

    take x*y, making sure that x*y + 2(x+y) <= n
    for example: x = 2, y = 3
        6 + 2*5 = 16 <= 22, so it's a valid check

    for each starting position, while not cut:
        if can add, must add
        if exceeded number, break
        if cannot add and not exceeded:
            if valid, count solution


    must hold:
    2xy + k(2x + 2y) = n
        2xy + 2k(x + y) = n
        2 (xy + k(x+y)) = n
        xy + k(x+y) = n/2

    For n = 22
    xy + k(x+y) = 11
    x=2, y=3, k=1 is a solution
    x=5, y=1, k=1 is a solution
    distinct solution sets -> 2
    C(22) = 2?

    for each solution of the equation
        result = result + inner_ways(x, y)

    return result
    '''


def blocks_needed(x, y, z, layer):
    result = 2 * (x*y + x*z + y*z)
    if layer >= 2:
        result = result + 4*(x+y+z) * (layer - 1)
    if layer >= 3:
        result = result + 8*(layer-2)*(layer-1)//2
    return result

assert blocks_needed(3, 2, 1, 1) == 22
assert blocks_needed(3, 2, 1, 2) == 46  # +24
assert blocks_needed(3, 2, 1, 3) == 78  # +24 + 8
assert blocks_needed(3, 2, 1, 4) == 118, blocks_needed(3, 2, 1, 4)  # +24 + 8 + 8

last_res = C(22)
assert last_res == 2, last_res
last_res = C(46)
assert last_res == 4, last_res
last_res = C(78)
assert last_res == 5, last_res
last_res = C(118)
assert last_res == 8, last_res
last_res = C(154)
assert last_res == 10, last_res

#print(C(100000))  # 100000 can be done from 1109 cuboids

def generate(n):
    sols = defaultdict(int)

    for x in range(1, n):
        for y in range(1, x + 1):
            x_times_y = x*y
            if x_times_y > n:
                break
            for z in range(1, y + 1):
                if x_times_y * z > n:
                    break
                fill_layers(n, x, y, z, sols)

    return sols

def fill_layers(n, x, y, z, sols):
    layer = 1
    blocks = blocks_needed(x, y, z, layer)

    while blocks < n:
        sols[blocks] = sols[blocks] + 1
        layer = layer + 1
        blocks = blocks_needed(x, y, z, layer)


sols = generate(200)
expected_sols = 10
for k, v in sols.items():
    if v == expected_sols:
        print(f'Solution with {expected_sols} sols: {k}')



def fill_2d(y, z, l):
    return 2*y + 2*z + 4*(l - 1)


assert fill_2d(3, 2, 2) == 14

def fill_3d(x, y, z, l):
    result = x * fill_2d(y, z, l)  # Fill the pure "inner blocks"
    result = result + 2*z*y  # Fill the outter most blocks
    # Original code for staircase blocks:
    # for layer in range(1, l):
    #     result = result + 2*fill_2d(y, z, layer)  # Fill the staircase blocks in between
    # Through some transformations we arrive to:
    if l >= 2:
        result = result + 4*(l - 1) * (y + z + l - 2)

    return result

assert fill_3d(5, 1, 1, 1) == 22, fill_3d(5, 1, 1, 1)
assert fill_3d(3, 2, 1, 1) == 22
assert fill_3d(3, 2, 1, 2) == 46
assert fill_3d(3, 2, 1, 3) == 78
assert fill_3d(3, 2, 1, 4) == 118
"""
filling(3, 2, 1, layer=1) = 3 * fill_2d(2, 1, layer=1) + 2 * fill_side(1, 2, 1, layer=0)

layer 0 means it is the outter layer, i.e., the count of blocks we need

"""

def generate2(n):
    sols = defaultdict(int)

    for x in range(1, n):
        for y in range(1, x + 1):
            x_times_y = x*y
            if x_times_y > n:
                break
            for z in range(1, y + 1):
                if x_times_y * z > n:
                    break
                fill_layers2(n, x, y, z, sols)

    return sols

def fill_layers2(n, x, y, z, sols):
    layer = 1
    blocks = fill_3d(x, y, z, layer)

    while blocks < n:
        sols[blocks] = sols[blocks] + 1
        layer = layer + 1
        blocks = fill_3d(x, y, z, layer)


sols = generate2(200000)
expected_sols = 1000
for k, v in sols.items():
    if v == expected_sols:
        print(f'Solution with {expected_sols} sols: {k}')  # Find min by hand from there

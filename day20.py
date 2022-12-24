from math import prod

test_mode = False

# test = '''1
# 2
# -3
# 3
# -2
# 0
# 4'''
test = '''1
2
-3
3
-2
0
4'''
# test = '''0
# -1
# -1
# 1
# '''
KEY = 811589153
with open('input/day20.sql') as f:
    text = f.read()

# coords = {int(j): i for i, j in enumerate((test if test_mode else text).splitlines())}
coords = [int(i)*KEY for i in (test if test_mode else text).splitlines()]
postion = [i for i in range(len((test if test_mode else text).splitlines()))]

N = len(coords)
for iteration in range(10):
    if test_mode:
        out = [None for _ in range(N)]
        for k, l in zip(coords, postion):
            out[l] = k
        print(out)
    for i, j in enumerate(coords):
        print((N*iteration+i)*100/(10*N), end="\r")

        if j != 0:
            og_index = postion[i]
            new_index = (og_index+j)
            # while new_index >= N:
            #     new_index -= N-1
            # while new_index < 0:
            #     new_index += N - 1
            # while new_index >= N:
            # while new_index < 0:
            #     new_index += N - 1

            new_index -= (N-1)*(new_index//(N-1))
            # elif new_index <= 0:
            #     new_index += (N - 1)*abs(new_index//(N-1))

            if og_index < new_index:
                postion = [(x-1) % N if og_index <= x <= new_index else x for x in postion]
            else:
                postion = [(x+1) % N if og_index >= x >= new_index else x for x in postion]

            postion[i] = new_index


# print(coords)
# instructions = coords.copy()
# if test_mode:
#     print(coords)
# for i in instructions:
#     if i != 0:
#         og_indx = []
#         for _ in range(coords.count(i)):
#             og_indx.append(coords.index(i, og_indx[-1]if len(og_indx) > 0 else 0))
#         print(og_indx)
#     # if test_mode:
#         # print(i, coords)


out = [None for _ in range(N)]
for k, l in zip(coords, postion):
    out[l] = k

if test_mode:
    print(out)

indx_0 = out.index(0)
a = [out[(indx_0+x) % len(coords)] for x in (1000, 2000, 3000)]
print(a)
print(sum(a))

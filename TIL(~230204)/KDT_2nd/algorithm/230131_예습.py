# 2차원 리스트가 있을 때 
# (1) 행 우선 순회 
# (2) 열 우선 순회를 직접 한번 해보기 (교재, 파이썬 보지 않고 해보기)
# (3) 이차원 리스트 총합, 최대값
# [ 
#   [1, 2, 3],
#   [4, 5, 6], 
#   [7, 8, 9]
# ]

# 1차원 리스트가 있을 때
# [1, 2, 3, 4, 5] => 1칸을 shift한다고 하면 [5, 1, 2, 3, 4]
import pprint
Y = 3
X = 4

list_2nd = []
for y in range(Y) :
        list_2nd.append([y*X + x for x in range(1, X+1)])

#print(list_2nd)

for y in range(Y) :
    for x in range(X) :
        if list_2nd[y][x] < 10 :
            print(' ',end='')
        print(list_2nd[y][x],end=' ')
    print()

print()

for y in range(Y) :
    for x in range(X) :
        print(list_2nd[y][x], end = ' ')
print()

for x in range(X) :
    for y in range(Y) :
        print(list_2nd[y][x], end = ' ')
print()

print()

sum_2nd = 0
for y in range(Y) :
    for x in range(X) :
       sum_2nd += list_2nd[y][x]
print(sum_2nd)

sum_2nd = 0
for y in range(Y) :
    sum_2nd += sum(list_2nd[y])
print(sum_2nd)

print()

max_2nd = 0 # 양수라고 가정
for y in range(Y) :
    for x in range(X) :
        if max_2nd < list_2nd[y][x] :
            max_2nd = list_2nd[y][x]
print(max_2nd)

max_2nd = 0
for y in range(Y) :
    if max_2nd < max(list_2nd[y]) :
        max_2nd = max(list_2nd[y])
print(max_2nd)

print()

# 2차원에서 한칸 쉬프트 앞으로 뒤로 \

# for y in range(Y) :
#     for x in range(X-1) :
#         list_2nd[y][x],list_2nd[y][x + 1] = list_2nd[y][x + 1],list_2nd[y][x]

# for y in range(Y) :
#     for x in range(X-1, 0, -1) :
#         list_2nd[y][x],list_2nd[y][x - 1] = list_2nd[y][x - 1],list_2nd[y][x]

# for y in range(Y-1) :
#     list_2nd[y],list_2nd[y+1] = list_2nd[y+1],list_2nd[y]

# for y in range(Y-1, 0, -1) :
#     list_2nd[y],list_2nd[y-1] = list_2nd[y-1],list_2nd[y]

for y in range(Y) :
    for x in range(X) :
        if list_2nd[y][x] < 10 :
            print(' ',end='')
        print(list_2nd[y][x],end=' ')
    print()

print()


for x in range(X-1) :
    list[x],list[x + 1] = list[x + 1],list[x]
    




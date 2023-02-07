# import sys
# sys.stdin = open('test.txt', 'r')
# import sys
# input = sys.stdin.readline

# 17608.
import sys
N = int(sys.stdin.readline())
list1 = [int(sys.stdin.readline()) for n in range(N)]
# print(list1)
max_num = 0
cnt = 0
for n in list1[::-1] :
    if n > max_num :
        max_num = n
        cnt += 1

print(cnt)


# 7568.
N = int(input())
list1 = [tuple(map(int,input().split())) for n in range(N)]
# print(list1)


for i in range(len(list1)) :
    rank = 1
    for j in range(len(list1)) :
        if i == j : continue
        if list1[i][0] < list1[j][0] and list1[i][1] < list1[j][1] :
            rank += 1
    print(rank, end=' ')
print()    


# 1063.
# input을 행렬로 변환
k, s, N = input().split()

k_dy = 8 - int(k[1])
k_dx = ord(k[0]) - ord('A')
s_dy = 8 - int(s[1])
s_dx = ord(s[0]) - ord('A')
# print(k_dy, k_dx, s_dy, s_dx)

dict_dxy = {
    'R'  : ( 0, 1),
    'L'  : ( 0,-1),
    'B'  : ( 1, 0),
    'T'  : (-1, 0),
    'RT' : (-1, 1),
    'LT' : (-1,-1),
    'RB' : ( 1, 1),
    'LB' : ( 1,-1)
}

for i in range(int(N)) :
    key = input()
    move = dict_dxy[key]
    if k_dy + move[0] == s_dy and k_dx + move[1] == s_dx :
        if 0 <= s_dy + move[0] < 8 and 0 <= s_dx + move[1] < 8 :
            s_dy += move[0]
            s_dx += move[1] 
            k_dy += move[0]
            k_dx += move[1] # 돌옮기고 킹 옮기기
    else : # 킹 이동 가능한지 판단하고 
        if 0 <= k_dy + move[0] < 8 and 0 <= k_dx + move[1] < 8 :
            k_dy += move[0]
            k_dx += move[1]
        
print(chr(k_dx + ord('A')) + str(8 - k_dy))
print(chr(s_dx + ord('A')) + str(8 - s_dy))


# 
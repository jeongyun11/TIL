import sys
sys.stdin = open('test.txt', 'r')

# # 10769.
# string = input()

# if (':-(' not in string) and (':-)' not in string) :
#     print('none')
# else :
#     # cnt = 0 
#     # cnt -= string.count(':-(')
#     # cnt += string.count(':-)')

#     cnt = 0
#     for i in range(len(string)-2) :
#         if string[i : i+2] == ':-' :
#             if string[i+2] == ')' : cnt += 1
#             if string[i+2] == '(' : cnt -= 1

#     if cnt < 0 : print('sad')
#     elif cnt > 0 : print('happy')
#     else : print('unsure')


# # 2455.
# max_num = 0
# cur = 0

# for i in range(4) :
#     o, i = map(int,input().split())
#     cur += i - o

#     max_num = max(cur, max_num)

# print(max_num)


# # 2606. 

# # # 인접 리스트

# # 1. 리스트 생성
# list1 = [[] for i in range(int(input()) + 1)]#for i in range(int(input())+1)]
# # print(list1)

# for i in range(int(input())) :
#     com1, com2 = map(int, input().split())
#     list1[com1].append(com2)
#     list1[com2].append(com1)
# # print(list1)

# 2. 탐색
# visited = [False] * len(list1)
# # print(visited)
# stack = [1]
# visited[1] = True
# while stack :
#     for com in list1[stack.pop()] :
#         if visited[com] == False :
#             stack.append(com)
#             visited[com] = True
#     # print(stack)

# print(visited.count(True) - 1)
# # for i in range(len(visited)) :
# #     if visited[i] == True :
# #         print(i, end=' ')
# # print()


# # # 4963.
# import sys
# # while True :
#     # if X == 0 or Y == 0 :
#     #     break
# X, Y = map(int, sys.stdin.readline().strip().split())
# matrix1 = [list(map(int, sys.stdin.readline().strip().split())) for y in range(Y)]
# # print(matrix1)

# list_land = []
# dict_land = {}
# for y in range(Y) :
#     for x in range(X) :
#         if matrix1[y][x] == 1 :
#             list_land.append((x,y))
#             dict_land[(x,y)] = []
# # print(list_land)
# # print(dict_land)

# for i in range(len(list_land)) :
#     for j in range(len(list_land)) :
#         if list_land[i] != list_land[j] :
#             if (list_land[i][0] - list_land[j][0]) in [-1, 0, 1] and (list_land[i][1] - list_land[j][1]) in [-1, 0, 1] :
#                 dict_land[list_land[i]].append(list_land[j])
# from pprint import pprint
# pprint(dict_land)

# visited = [False] * len(list_land)
# # print(visited)

# cnt = 0
# while False in visited :
#     i = visited.index(False)
#     stack = [list_land[i]]
#     visited[i] = True

#     while stack :
#         # print(stack)
#         for land in dict_land[stack.pop()] :
#             list_land.index(land)
#             if visited[list_land.index(land)] == False :
#                 stack.append(land)
#                 visited[list_land.index(land)] = True
#     cnt += 1

# print(cnt)

# ---------------------------
# 한 번 풀고

# def remove_land(matrix, stack, dxdy) : # stack에 담긴 좌표에 포함되는 land를 0으로 바꾸는 함수
#     while stack :
#         y, x = stack.pop()
#         for y1, x1 in dxdy : 
#             y_move = y + y1
#             x_move = x + x1
#             if 0 <= x_move < len(matrix[0]) and 0 <= y_move < len(matrix): # 행렬의 범위를 안 벗어나고
#                 if matrix[y_move][x_move] == 1 :# 그 값이 1이면
#                     stack.append((y + y1, x + x1)) # 추가한다.
#         matrix[y][x] = 0

# while True :
#     X, Y = map(int,input().split())

#     if X == Y == 0 :
#         break

#     matrix = [list(map(int,input().split())) for y in range(Y)]
#     cnt = 0

#     for y in range(Y) :
#         for x in range(X) :
#             if matrix[y][x] == 1 : # 순회하며 1이면 
#                 stack = [(y, matrix[y].index(1))] # 그 좌표를 stack에 넣어주고
#                 remove_land(matrix, stack, [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]) # 포함된 land를 0으로 바꾼다.
#                 cnt +=1 # land가 사라질 때마다 +1

#     print(cnt)


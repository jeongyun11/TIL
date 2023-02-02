import sys
sys.stdin = open('test.txt', 'r')


# # 2441. 
# N = int(input())

# for n in range(N) :
#     print(' '*n + '*'*(N-n))


# # 2592.

# numbers = [int(input()) for i in range(10)]
# numbers_dict = {}
# for number in numbers :
#     numbers_dict[number] = numbers_dict.get(number,0) + 1

# print(round(sum(numbers)/len(numbers)))
# print(sorted(numbers_dict.items(), key = lambda x : x[1], reverse=True)[0][0])


# # 10798.
# words = [list(input()) for i in range(5)]
# Y = 5
# X = len(max(words,key=len))

# for y in range(Y) :
#     if len(words[y]) < X :
#         for i in range(X - len(words[y])) :
#             words[y].append(None)


# for x in range(X) :
#     for y in range(Y) :
#         if words[y][x] == None :
#             continue
#         print(words[y][x], end='')


# 9455.
# x와 y 대칭
T = int(input())
for _ in range(T) :
    Y, X = map(int,input().split())
    matrix = [list(map(int, input().split()))for y in range(Y)]

    # 열 우선 탐색으로 아래부터 블럭을 내려준다
    # - 블럭이 바닥에서 멈추게 한다.
    cnt = 0
    for x in range(X) :
        for y in range(Y-2, -1, -1) : # 마지막 줄을 제외하고 아래에서 위로
            while True :
                if (matrix[y][x] == 1) :
                    if (y+1 == len(matrix)) :
                        break
                    elif (matrix[y+1][x] == 1) :
                        break
                    else :
                        matrix[y+1][x] = 1 
                        matrix[y][x] = 0
                        y += 1
                        cnt += 1
                else :
                    break
    print(cnt)

# T = int(input())
# for t in range(T) :
#     X, Y = map(int, input().split())
#     matrix = [list(map(int, input().split())) for x in range(X)]
#     matrix_2 = [[0 for x in range(X)] for y in range(Y)]

#     for x in range(X) :
#         for y in range(Y) :
#             matrix_2[y][x] = matrix[x][y]

#     cnt = 0
#     for y in range(Y) :
#         for x in range(X) :
#             if matrix_2[y][x] == 1 :
#                 cnt += matrix_2[y][x+1:].count(0)
#     print(cnt)




    
# # 1652.
# Y = int(input())
# X = Y


# matrix = [list(input()) for y in range(Y)]

# matrix2 = [[[0] for x in range(X)] for y in range(Y)]
# for y in range(Y) :
#     for x in range(X) :
#         matrix2[y][x] = matrix[x][y]

# result1, result2 = 0, 0

# for y in range(Y) :
#     matrix[y].append('X')

# for y in range(Y) :
#     cnt = 0
#     for x in range(X+1) :
#         if matrix[y][x] == '.' :
#             cnt +=1
            
#         else :
#             if cnt >= 2 :
#                 result1 += 1
#             cnt = 0
        

# for y in range(Y) :
#     matrix2[y].append('X')

# for y in range(Y) :
#     cnt = 0
#     for x in range(X+1) :
#         if matrix2[y][x] == '.' :
#             cnt +=1
#         else :
#             if cnt >= 2 :
#                 result2 += 1
#             cnt = 0
        
# print(result1, result2)

